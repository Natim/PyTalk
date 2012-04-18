#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, datetime
from PyQt4.QtGui import *
from PyQt4.QtCore import SIGNAL, SLOT, Qt, QSize
from ui.ui_mainwindow import Ui_MainWindow

from AboutDialog import AboutDialog
from ConnectionDialog import ConnectionDialog
from ConnectorThread import ConnectorThread
from MessageBox import MessageBox
from BuddyList import BuddyList
from RosterRequest import RosterRequest
from AddBuddyDialog import AddBuddyDialog
from AddGroupDialog import AddGroupDialog

from jabber import STATUS

class MainWindow(QMainWindow, Ui_MainWindow):
    connectorThread = None

    def __init__(self, parent = None):
    
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
        self.console = QDialog()
        self.te = QTextEdit(self.console)
        self.te.setReadOnly(True)
        vl = QVBoxLayout()
        vl.addWidget(self.te)
        self.console.setLayout(vl)
        
        # Set status Offline
        self.statusBox.setCurrentIndex(5)
        self.statusEdit.hide()

        # Set connect
        self.connect(self.statusBox, SIGNAL("currentIndexChanged(int)"), self.changeStatus)
        self.connect(self.statusEdit, SIGNAL("returnPressed()"), self.changeStatus)

        # Set BuddyList
        self.BuddyList = BuddyList(self)
        self.vboxlayout.insertWidget(0, self.BuddyList)
        self.connect(self.BuddyList, SIGNAL("rename"), self.addBuddy)

        # Connection
        connection = ConnectionDialog(self)
        self.connect(self.actionConnection, SIGNAL("triggered()"), connection, SLOT("exec()"))
        self.connect(self.actionDeconnection, SIGNAL("triggered()"), self.disconnect)
        self.connect(connection, SIGNAL("configured()"), self.connection)

        # Contacts
        self.connect(self.actionAdd_a_buddy, SIGNAL("triggered()"), self.addBuddy)
        self.connect(self.actionAdd_a_group, SIGNAL("triggered()"), self.addGroup)

        # View
        self.connect(self.actionAway_buddies, SIGNAL("toogled()"), self.setAway)
        self.connect(self.actionOffline_buddies, SIGNAL("toogled()"), self.setOffline)
        self.connect(self.actionAway_buddies, SIGNAL("triggered()"), self.setAway)
        self.connect(self.actionOffline_buddies, SIGNAL("triggered()"), self.setOffline)

        # Tools
        self.connect(self.actionConsole, SIGNAL("triggered()"), self.swapConsole)
        
        # About Dialog
        about = AboutDialog(self)
        self.connect(self.actionAbout, SIGNAL("triggered()"), about, SLOT("exec()"))
        self.connect(self.actionAboutQt, SIGNAL("triggered()"), QApplication.instance(), SLOT("aboutQt()"))
        
        # Quit Signal connection
        self.connect(self.actionQuit, SIGNAL("triggered()"), self.quit)

    def connection(self, status=STATUS.available):
        if not self.connectorThread:
            self.connectorThread = ConnectorThread(status)
            self.connectorThread.start()
            self.connect(self.connectorThread, SIGNAL("message"), self.BuddyList.message)
            self.connect(self.connectorThread, SIGNAL("error"), self.error)
            self.connect(self.connectorThread, SIGNAL("connected()"), self.connected)
            self.connect(self.connectorThread, SIGNAL("disconnected()"), self.disconnect)
            self.connect(self.connectorThread, SIGNAL("presence"), self.BuddyList.presence)
            self.connect(self.connectorThread, SIGNAL("debug"), self.debug)
            self.connect(self.connectorThread, SIGNAL("subscriptionRequest"), self.subscriptionRequest)
            self.connect(self.connectorThread, SIGNAL("addBuddy"), self.addBuddy)
        elif self.connectorThread.isConnected():
            self.connectorThread.changeStatus(status, self.statusEdit.text())
            self.statusEdit.clearFocus()

    def disconnect(self):
        self.actionConnection.setEnabled(True)
        self.actionDeconnection.setEnabled(False)
        self.statusEdit.hide()
        self.statusBox.setCurrentIndex(STATUS.unavailable.index)
        if self.connectorThread:
            self.connectorThread.disconnect()
            self.connectorThread = None
        self.BuddyList.clear()
        QApplication.instance().quit()
        
            
    def connected(self):
        self.actionConnection.setEnabled(False)
        self.actionDeconnection.setEnabled(True)
        if self.statusBox.currentIndex() == STATUS.unavailable.index:
            self.statusBox.setCurrentIndex(STATUS.available.index)
        else:
            self.connectorThread.changeStatus(self.statusBox.currentIndex(), self.statusEdit.text())
        self.statusEdit.show()
        self.statusEdit.setFocus()
        self.BuddyList.setConnection(self.connectorThread)
        self.getRoster()
        self.setAway()
        self.setOffline()

    def error(self, title, content):
        QMessageBox.critical(self, title, content, QMessageBox.Ok)

    def closeEvent(self, event):
        self.quit()

    def quit(self):
        self.disconnect()

    def changeStatus(self, index=-1):
        if index == -1:
            index = self.statusBox.currentIndex()
        if index == STATUS.unavailable.index:
            self.statusEdit.hide()
            self.disconnect()
        else:
            self.connection(index)

    def getRoster(self):
        roster = self.connectorThread.getRoster()
        for buddy in roster:
            self.BuddyList.addItem(buddy)
        self.connect(self.BuddyList, SIGNAL("itemDoubleClicked(QTreeWidgetItem *,int)"), self.sendMessage)

    def sendMessage(self, item, col):
        if item and item.type() == QTreeWidgetItem.UserType+1:
            item.sendMessage()
            
    def setAway(self, checked=-1):
        if checked == -1:
            checked = self.actionAway_buddies.isChecked()
        self.BuddyList.setAway(not checked)
            
    def setOffline(self, checked=-1):
        if checked == -1:
            checked = self.actionOffline_buddies.isChecked()
        self.BuddyList.setOffline(not checked)

    def subscriptionRequest(self, presence):
        request = RosterRequest(self, self.connectorThread.jabber, presence)
        request.show()

    def debug(self, message):
        self.te.append(datetime.datetime.now().strftime("[%H:%M:%S]")+" : \n"+message)

    def swapConsole(self):
        self.console.setWindowTitle("XML Console")
        self.console.resize(QSize(1024, 500))
        self.console.show()
        self.console.raise_()

    def addBuddy(self, item=None):
        if self.connectorThread:
            if item:
                jid = item.jid
            else:
                jid = ""
            newBuddy = AddBuddyDialog(self, self.connectorThread.jabber, self.BuddyList.groups.keys(), jid)
            newBuddy.show()

    def addGroup(self):
        newGroup = AddGroupDialog(self, self.BuddyList)
        newGroup.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
