from PyQt4.QtGui import QDialog
from PyQt4.QtCore import Qt, SIGNAL

from ui.ui_AddGroupDialog import Ui_AddGroupDialog
import xmpp

class AddGroupDialog(QDialog, Ui_AddGroupDialog):
    def __init__(self, parent, BuddyList):
        QDialog.__init__(self, parent)
        self.parent = parent
        self.setupUi(self)
        self.BuddyList = BuddyList
        self.connect(self, SIGNAL("accepted()"), self.add)

    def add(self):
        self.BuddyList.addGroup(self.group.text())
        
