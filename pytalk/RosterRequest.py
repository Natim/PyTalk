from PyQt4.QtGui import QDialog
from PyQt4.QtCore import Qt, SIGNAL, SLOT

import xmpp

from ui.ui_BuddiesListRequest import Ui_BuddiesListRequest

class RosterRequest(QDialog, Ui_BuddiesListRequest):
    """BuddyList implements the view in a Tree of the Roster"""

    def __init__(self, parent, jabber, presence):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent
        self.jabber = jabber
        self.jid = presence.getFrom().getStripped()
        self.presence = presence
        if presence.getStatus():
            status = presence.getStatus()
        else:
            status =""
        self.textEdit.setText(self.jid+self.tr(" would like to add you on his Buddies List\n\n")+status)

        self.connect(self, SIGNAL("accept()"), self.accept)
        self.connect(self, SIGNAL("reject()"), self.reject)


    def accept(self):
        reply = xmpp.protocol.Presence(to=self.presence.getFrom().getStripped(), typ="subscribed")
        self.parent.debug(unicode(reply)+"\n")
        self.jabber.send(reply)
        self.close()

    def reject(self):
        reply = xmpp.protocol.Presence(to=self.presence.getFrom().getStripped(), typ="unsubscribed")
        self.parent.debug(unicode(reply)+"\n")
        self.jabber.send(reply)
