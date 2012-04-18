from PyQt4.QtGui import QTreeWidgetItem, QIcon, QDialog, QVBoxLayout, QApplication, QMenu
from PyQt4.QtCore import Qt, QVariant, QSettings

from MessageBox import MessageBox
from AddBuddyDialog import AddBuddyDialog

from jabber import STATUS
from jabber import STATUS_IMAGE

class BuddyItem(QTreeWidgetItem):
    """
      BuddyItem implements the view of a Buddy from the Roster
    """

    dialog = None
    msg = None

    def __init__(self, parent, jid, con):
        QTreeWidgetItem.__init__(self, parent, [jid], QTreeWidgetItem.UserType+1)

        # QTreeWidgetItem configuration
        self.setFlags(Qt.ItemIsDragEnabled | Qt.ItemIsEnabled) # we can move a contact
        self.parent = parent
        self.jid = jid
        self.name = jid
        self.setStatus(STATUS.unavailable)
        self.connectionThread = con
    
    def setStatus(self, status):
        self.status = status
        if self.status.index not in range(6):
            self.status = STATUS.unavailable
        settings = QSettings("Trunat", "PyTalk")
        settings.beginGroup("preferences")
        repStatus = settings.value("images_status", QVariant("images/status/")).toString()
        fileStatus = settings.value(str(self.status), QVariant(STATUS_IMAGE[self.status.index])).toString()
        settings.endGroup()
        self.setIcon(0, QIcon(repStatus+fileStatus))

    def setName(self, name):
        if name:
            self.name = name
            self.setText(0, name)

    def status(self):
        return status

    def isAway(self):
        return (self.status == STATUS.away or self.status == STATUS.xa)

    def isOffline(self):
        if self.status == STATUS.unavailable:
            return True
        else:
            return False

    def createDialog(self):
        if not self.dialog:
            self.dialog = QDialog()
            self.dialog.setWindowIcon(QIcon("images/mail.png"))

            self.msg = MessageBox(self.dialog, self.connectionThread, self.jid, self.name)
            layout = QVBoxLayout(self.dialog)
            layout.addWidget(self.msg)
            self.dialog.setLayout(layout)
            self.dialog.setWindowTitle(self.dialog.tr("Chat with ") + self.name)
        self.dialog.show()
        self.dialog.raise_()

    def receiveMessage(self, event):
        self.createDialog()
        self.msg.receiveMessage(event)

    def sendMessage(self):
        self.createDialog()

    def __str__(self):
        return u'%s' % self.name
