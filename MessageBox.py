from PyQt4.QtGui import QWidget, QIcon
from PyQt4.QtCore import QSettings, QVariant, SIGNAL
from ui.ui_MessageWidget import Ui_MessageWidget
import md5, webbrowser

class MessageBox(QWidget, Ui_MessageWidget):
    def __init__(self, parent, con, jid, name):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.jid = jid
        self.name = name
        self.con = con

        self.messageBrowser.setPlainText("")
        self.messageBrowser.setOpenLinks(False)

        self.messageEdit.setFocus()

        self.connect(self.sendButton, SIGNAL("clicked()"), self.sendMessage)
        self.connect(self.videoButton, SIGNAL("clicked()"), self.startVideo)
        self.connect(self.messageBrowser, SIGNAL("anchorClicked(QUrl)"), self.openLink)

    def receiveMessage(self, event):
        message = """\n<strong><span style="color: darkblue">%s :</span></strong> %s""" % (self.name, event.getBody())
        self.messageBrowser.append(message)

    def sendMessage(self):
        if self.messageEdit.text():
            message = """\n<strong><em><span style="color: darkred">%s :</span></em></strong> %s""" % (self.tr("Me"), self.messageEdit.text())
            self.messageBrowser.append(message)
            self.con.send_message(self.jid, self.messageEdit.text())
            self.messageEdit.clear()
            
    def startVideo(self):
        hash = md5.new(self.jid).hexdigest()
        url = "http://jtalk.trunat.fr/jtalk/?%s" % (hash)
        message = """\n<a href="%s">Click here to join the videoChat</a>""" % (url)
        self.messageBrowser.append(message)
        self.con.send_message(self.jid, "Join me for a video chat here : %s" % url)
        webbrowser.open(url)

    def openLink(self, url):
        webbrowser.open(url.toString())
