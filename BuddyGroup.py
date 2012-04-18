from PyQt4.QtGui import QTreeWidgetItem
from PyQt4.QtCore import Qt

class BuddyGroup(QTreeWidgetItem):
    """
      BuddyGroup implements the view of a Buddy group from the Roster
    """

    def __init__(self, name):
        QTreeWidgetItem.__init__(self, [name], QTreeWidgetItem.UserType+0)

        self.name = name
        # QTreeWidgetItem configuration
        self.setFlags(Qt.ItemIsDropEnabled | Qt.ItemIsEnabled) # We can move a contact into
        
    def isAway(self):
        for child in self.takeChildren():
            if not child.isAway():
                return False
        return True

    def isOffline(self):
        for child in self.takeChildren():
            if not child.isOffline():
                return False
        return True
        
