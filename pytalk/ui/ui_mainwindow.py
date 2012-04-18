# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created: Thu Jan 24 11:09:31 2008
#      by: PyQt4 UI code generator 4.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,316,407).size()).expandedTo(MainWindow.minimumSizeHint()))
        MainWindow.setWindowIcon(QtGui.QIcon("images/im-jabber.png"))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.vboxlayout = QtGui.QVBoxLayout(self.centralwidget)
        self.vboxlayout.setObjectName("vboxlayout")

        self.statusBox = QtGui.QComboBox(self.centralwidget)
        self.statusBox.setObjectName("statusBox")
        self.vboxlayout.addWidget(self.statusBox)

        self.statusEdit = QtGui.QLineEdit(self.centralwidget)
        self.statusEdit.setObjectName("statusEdit")
        self.vboxlayout.addWidget(self.statusEdit)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,316,29))
        self.menubar.setObjectName("menubar")

        self.menuContacts = QtGui.QMenu(self.menubar)
        self.menuContacts.setObjectName("menuContacts")

        self.menuAffichage = QtGui.QMenu(self.menubar)
        self.menuAffichage.setObjectName("menuAffichage")

        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        self.menuBuddies = QtGui.QMenu(self.menubar)
        self.menuBuddies.setObjectName("menuBuddies")

        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)

        self.actionConnection = QtGui.QAction(MainWindow)
        self.actionConnection.setIcon(QtGui.QIcon("images/status/log-in.png"))
        self.actionConnection.setObjectName("actionConnection")

        self.actionDeconnection = QtGui.QAction(MainWindow)
        self.actionDeconnection.setEnabled(False)
        self.actionDeconnection.setIcon(QtGui.QIcon("images/status/log-out.png"))
        self.actionDeconnection.setObjectName("actionDeconnection")

        self.actionOffline_buddies = QtGui.QAction(MainWindow)
        self.actionOffline_buddies.setCheckable(True)
        self.actionOffline_buddies.setObjectName("actionOffline_buddies")

        self.actionAway_buddies = QtGui.QAction(MainWindow)
        self.actionAway_buddies.setCheckable(True)
        self.actionAway_buddies.setChecked(True)
        self.actionAway_buddies.setObjectName("actionAway_buddies")

        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setIcon(QtGui.QIcon("images/about.png"))
        self.actionAbout.setObjectName("actionAbout")

        self.actionAboutQt = QtGui.QAction(MainWindow)
        self.actionAboutQt.setIcon(QtGui.QIcon("images/qt4.png"))
        self.actionAboutQt.setObjectName("actionAboutQt")

        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setIcon(QtGui.QIcon("images/exit.png"))
        self.actionQuit.setObjectName("actionQuit")

        self.actionAdd_a_buddy = QtGui.QAction(MainWindow)
        self.actionAdd_a_buddy.setIcon(QtGui.QIcon("images/plus.png"))
        self.actionAdd_a_buddy.setObjectName("actionAdd_a_buddy")

        self.actionAdd_a_group = QtGui.QAction(MainWindow)
        self.actionAdd_a_group.setIcon(QtGui.QIcon("images/plus.png"))
        self.actionAdd_a_group.setObjectName("actionAdd_a_group")

        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setIcon(QtGui.QIcon("images/preferences.png"))
        self.actionPreferences.setObjectName("actionPreferences")

        self.actionConsole = QtGui.QAction(MainWindow)
        self.actionConsole.setObjectName("actionConsole")
        self.menuContacts.addAction(self.actionConnection)
        self.menuContacts.addAction(self.actionDeconnection)
        self.menuContacts.addAction(self.actionQuit)
        self.menuAffichage.addAction(self.actionOffline_buddies)
        self.menuAffichage.addAction(self.actionAway_buddies)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAboutQt)
        self.menuBuddies.addAction(self.actionAdd_a_buddy)
        self.menuBuddies.addAction(self.actionAdd_a_group)
        self.menuTools.addAction(self.actionPreferences)
        self.menuTools.addAction(self.actionConsole)
        self.menubar.addAction(self.menuContacts.menuAction())
        self.menubar.addAction(self.menuBuddies.menuAction())
        self.menubar.addAction(self.menuAffichage.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PyTalk", None, QtGui.QApplication.UnicodeUTF8))
        self.statusBox.addItem(QtGui.QIcon("images/status/available.png"),QtGui.QApplication.translate("MainWindow", "Available", None, QtGui.QApplication.UnicodeUTF8))
        self.statusBox.addItem(QtGui.QIcon("images/status/chat.png"),QtGui.QApplication.translate("MainWindow", "Chat", None, QtGui.QApplication.UnicodeUTF8))
        self.statusBox.addItem(QtGui.QIcon("images/status/busy.png"),QtGui.QApplication.translate("MainWindow", "Do not disturb", None, QtGui.QApplication.UnicodeUTF8))
        self.statusBox.addItem(QtGui.QIcon("images/status/away.png"),QtGui.QApplication.translate("MainWindow", "Away", None, QtGui.QApplication.UnicodeUTF8))
        self.statusBox.addItem(QtGui.QIcon("images/status/extended-away.png"),QtGui.QApplication.translate("MainWindow", "Extended Away", None, QtGui.QApplication.UnicodeUTF8))
        self.statusBox.addItem(QtGui.QIcon("images/status/offline.png"),QtGui.QApplication.translate("MainWindow", "Offline", None, QtGui.QApplication.UnicodeUTF8))
        self.menuContacts.setTitle(QtGui.QApplication.translate("MainWindow", "Account", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAffichage.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuBuddies.setTitle(QtGui.QApplication.translate("MainWindow", "Buddies", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("MainWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConnection.setText(QtGui.QApplication.translate("MainWindow", "L&og in", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConnection.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeconnection.setText(QtGui.QApplication.translate("MainWindow", "Log out", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOffline_buddies.setText(QtGui.QApplication.translate("MainWindow", "Offline buddies", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAway_buddies.setText(QtGui.QApplication.translate("MainWindow", "Away buddies", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About pyTalk", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAboutQt.setText(QtGui.QApplication.translate("MainWindow", "About Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_a_buddy.setText(QtGui.QApplication.translate("MainWindow", "Add a buddy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_a_group.setText(QtGui.QApplication.translate("MainWindow", "Add a group", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "&Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConsole.setText(QtGui.QApplication.translate("MainWindow", "XML Console", None, QtGui.QApplication.UnicodeUTF8))

