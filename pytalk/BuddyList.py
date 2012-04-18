from PyQt4.QtGui import QTreeWidget, QTreeWidgetItem, QMenu, QIcon
from PyQt4.QtCore import Qt, SIGNAL

from BuddyItem import BuddyItem
from BuddyGroup import BuddyGroup

import time

class BuddyList(QTreeWidget):
    """BuddyList implements the view in a Tree of the Roster"""

    def __init__(self, parent):
        QTreeWidget.__init__(self, parent)
        self.connection = None
        # QTreeWidgetItem configuration
        self.header().hide()
        self.setSortingEnabled(True)
        self.sortItems(0, Qt.AscendingOrder)
        self.buddies = {}
        self.groups  = {}
        self.tree    = {}

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.menu = QMenu()
        self.menu.addAction(QIcon("images/rename.png"), "Rename", self.rename)
        self.menu.addAction(QIcon("images/infos.png"), "User Infos", self.getInfo)

        self.connect(self, SIGNAL("customContextMenuRequested(QPoint)"), self.context)

        self.offline = True
        self.away = False
        
    def setConnection(self, con):
        self.connection = con
        
    def addItem(self, jid):
        if self.connection:
            group = self.connection.getGroups(jid)[0]
            self.addGroup(group)
            if jid not in self.buddies.keys():
                self.buddies[jid] = BuddyItem(self.groups[group],jid, self.connection)
                self.buddies[jid].setName(self.connection.getName(jid))
            self.groups[group].addChild(self.buddies[jid])
            self.tree[group][jid] = self.buddies[jid]
        
    def addGroup(self, group):
        if group:
            if group not in self.groups.keys():
                self.groups[group] = BuddyGroup(group)
                self.tree[group] = {}
                self.addTopLevelItem(self.groups[group])

    def setOffline(self, hide):
        self.offline = hide
        self.hideGroups()  

    def setAway(self, hide):
        self.away = hide
        self.hideGroups()
        
    def hideGroups(self):
        for child in self.buddies.values():
            if child.isOffline():
                child.setHidden(self.offline)
            elif child.isAway():
                child.setHidden(self.away)
            else:
                child.setHidden(False)

        for group in self.tree.keys():
            hide = True
            for child in self.tree[group].values():
                if not child.isHidden():
                    hide = False
            self.groups[group].setHidden(hide)
        self.expandAll()

    def message(self, event):
        buddy = event.getFrom().getStripped()
        if buddy not in self.buddies.keys():
            self.buddies[buddy] = BuddyItem(None, buddy)
        self.buddies[buddy].receiveMessage(event)

    def presence(self, jid, status, show=None):
        if jid in self.buddies.keys():
            self.buddies[jid].setStatus(status)
        else:
            time.sleep(2.0)
            self.presence(jid, status, show)
        self.hideGroups()

    def context(self, pos):
        item = self.itemAt(pos)
        if item:
            if item.type() == QTreeWidgetItem.UserType+1:
                self.currentItem = item
                self.menu.popup(self.mapToGlobal(pos))
        

    def rename(self):
        self.emit(SIGNAL("rename"), self.currentItem)

    def getInfo(self):
        pass
