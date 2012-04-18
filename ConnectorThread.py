import time
import xmpp
import sys
import settings
import platform
from PyQt4.QtCore import QSettings, QVariant, QThread, SIGNAL
from PyQt4.QtGui import QMessageBox
from jabber import STATUS

class ConnectorThread(QThread):
    """
       ConnectorThread is the class which manage the connection between the
       Jabber server and the PyTalk client.
    """

    def __init__(self, status):
        "We initialise a new Thread and create the connection with the Jabber Server"
        QThread.__init__(self)
        self.status = status
    
    def run(self):
        "We are running the thread and are reading and sending informations to the Jabber server"

        if self.connect():
            self.Terminated = False
            self.emit(SIGNAL("connected()"))
        else:
            self.Terminated = True

        while not self.Terminated:
            self.jabber.Process(1)
            time.sleep(2.0)
        sys.stderr.write('Thread correctly stopped'+unicode(self.Terminated)+'\n\n')

    def connect(self):
        settings = QSettings("Trunat", "PyTalk")
        settings.beginGroup("Connection")

        self.userID     = settings.value("userID").toString().__str__()
        self.password   = settings.value("password").toString().__str__()
        self.server     = settings.value("server").toString().__str__()
        self.useSSL     = settings.value("useSSL", QVariant(True)).toBool()

        if self.useSSL:
            self.port   = settings.value("port", QVariant("5223")).toInt()
        else:
            self.port   = settings.value("port", QVariant("5222")).toInt()

        self.port = int(self.port[0])

        self.ressource  = settings.value("ressource", QVariant("PyTalk")).toString().__str__()
        
        settings.endGroup()

        self.jid        = xmpp.protocol.JID(self.userID.__str__())
        self.jabber     = xmpp.Client(self.jid.getDomain(), debug=[])

        if self.server:
            server = (self.server, self.port)
        else:
            server = None
        connection = self.jabber.connect(server)
        
        if not connection:
            self.emit(SIGNAL("error"), self.tr("Connection Error"), self.tr("Could not connect"))
            return False
        sys.stderr.write('Connected with %s\n' % connection)
        
        auth = self.jabber.auth(self.jid.getNode(), self.password, self.ressource)
        if not auth:
            self.emit(SIGNAL("error"), self.tr("Authentication Error"), self.tr("Could not authenticate"))
            return False
        sys.stderr.write('Authenticate using %s\n' % auth)

        self.register_handlers()
        self.jabber.sendInitPresence(requestRoster=1)

        return connection

    def disconnect(self):
        "We stop to speak with the server and disconnect from it"
        self.Terminated = True
        if self.jabber.isConnected():
            self.jabber.disconnect()

    def register_handlers(self):
        self.jabber.RegisterHandler('message', self.xmpp_message)
        self.jabber.RegisterHandler("iq", self.handle_version, typ = "get", ns = xmpp.NS_VERSION)
        self.jabber.RegisterHandler("iq", self.handle_disco_info, typ = "get", ns = xmpp.NS_DISCO_INFO)
        self.jabber.RegisterHandler("iq", self.rosterChange, typ = "set", ns = xmpp.NS_ROSTER)
        self.jabber.RegisterHandler("presence", self.subscriptionRequest, typ = "subscribe")
        self.jabber.RegisterHandler("presence", self.addBuddy, typ = "suscribed")
        self.jabber.RegisterHandler("presence", self.presence)
        self.jabber.RegisterHandler("iq", self.request)
        self.jabber.RegisterDisconnectHandler(lambda: self.emit(SIGNAL("connect()")))

    def request(self, con, packet):
        self.emit(SIGNAL("debug"), unicode(packet)+"\n\n")

    def xmpp_message(self, con, event):
        self.emit(SIGNAL("debug"), unicode(event)+"\n\n")
        type = event.getType()
        if type:
            if type in ['message', 'chat']:
                message = event.getBody()
                if message:
                    self.emit(SIGNAL("message"), event)

    def send_message(self, tojid, message):
        m = xmpp.protocol.Message(to=tojid, body=message, typ='chat')
        
        self.emit(SIGNAL("debug"), unicode(m)+"\n\n")
        self.jabber.send(m)

    def changeStatus(self, showId, status):
        """Send a presence packet"""
        p = xmpp.protocol.Presence()
        p.setShow(STATUS[showId])
        if status:
            p.setStatus(status)
        if showId == STATUS.available:
            p.setPriority(5)
        self.jabber.send(p)
        self.emit(SIGNAL("debug"), unicode(p)+"\n\n")

    def handle_version(self, con, iq):
        """Respond to a version info request."""
        self.emit(SIGNAL("debug"), unicode(iq)+"\n")
        reply = iq.buildReply('result')
        #add <name/> and <version/> in accordance with XEP-0092
        reply.T.query.addChild(name="name", payload=settings.APPNAME)
        reply.T.query.addChild(name="version", payload=settings.VERSION)
        if platform.mac_ver()[0]:
            plateforme = "Mac OS %s" % platform.mac_ver()[0] 
        elif platform.win32_ver()[0]:
            plateforme = "Windows %s" % platform.win32_ver()[0]
        else:
            plateforme = "%s %s" % (platform.uname()[0], platform.uname()[2])
        reply.T.query.addChild(name="os", payload=plateforme)
        
        self.emit(SIGNAL("debug"), unicode(reply)+"\n")
        self.jabber.send(reply)

    def handle_disco_info(self, con, iq):
        self.emit(SIGNAL("debug"), unicode(iq)+"\n")
        reply = iq.buildReply('result')
        reply.T.query.addChild(name="feature", attrs={'var':'jabber:iq:version'})
        self.emit(SIGNAL("debug"), unicode(reply)+"\n")
        self.jabber.send(reply)

    def getRoster(self):
        self.roster = self.jabber.getRoster()
        return self.roster.getItems()
        
        
    def getGroups(self, jid):
        if self.roster.getGroups(jid):
            return self.roster.getGroups(jid)
        else:
            return ['Buddies']

    def getName(self, jid):
        return self.roster.getName(jid)

    def getStatus(self, jid):
        pass

    def presence(self, con, presence):
        # Somebody change his presence
        # Usefull Informations : 
        #  - typ is unavailable -> Contact gone offline
        self.emit(SIGNAL("debug"), unicode(presence)+"\n")
        jid = presence.getFrom().getStripped()
        if presence.getType() == "unavailable":
            self.emit(SIGNAL("presence"), jid, unicode(STATUS.unavailable))
        if not presence.getType():
            if not presence.getShow():
                self.emit(SIGNAL("presence"), jid, STATUS.available, presence.getStatus())
            else:
                status = presence.getShow()
                if status == "chat":
                    stat = STATUS.chat
                elif status == "dnd":
                    stat = STATUS.dnd
                elif status == "away":
                    stat= STATUS.away
                elif status == "xa":
                    stat = STATUS.xa
                else:
                    stat = STATUS.available
                self.emit(SIGNAL("presence"), jid, stat, presence.getStatus())
                

    def subscriptionRequest(self, con, presence):
        self.emit(SIGNAL("debug"), unicode(presence)+"\n")
        self.emit(SIGNAL("subscriptionRequest"), presence)

    def addBuddy(self, con, presence):
        self.emit(SIGNAL("debug"), unicode(presence)+"\n")
        self.emit(SIGNAL("addBuddy"), presence)

    def rosterChange(self, con, iq):
        self.emit(SIGNAL("rosterChange"), iq)
        
    def isConnected(self):
        return self.jabber.isConnected()

