from PyQt4.QtGui import QDialog
from PyQt4.QtCore import Qt, SIGNAL

from ui.ui_AddBuddyDialog import Ui_AddBuddyDialog
import xmpp

class AddBuddyDialog(QDialog, Ui_AddBuddyDialog):
    def __init__(self, parent, jabber, groups, jid="", group=""):
        QDialog.__init__(self, parent)
        self.parent = parent
        self.setupUi(self)
        self.jabber = jabber
        self.jid.setText(jid)
        self.group.addItems(groups)
        self.connect(self, SIGNAL("accepted()"), self.add)

    def add(self):
        result = xmpp.protocol.Iq(typ='set')
        result.setQueryNS(xmpp.NS_ROSTER)
        if self.nickname.text():
            item = xmpp.simplexml.Node(tag="item", attrs={"name": self.nickname.text(), "jid": self.jid.text()})
        else:
            item = xmpp.simplexml.Node(tag="item",
                                       attrs={"jid": self.jid.text()})
        item.addChild(name="group", payload=self.group.currentText())
        result.T.query.addChild(node=item)
        self.parent.debug(unicode(result)+"\n")
        self.jabber.send(result)
        presence = xmpp.protocol.Presence(to=str(self.jid.text()),  typ="subscribe")
        self.parent.debug(unicode(presence))
        self.jabber.send(presence)
