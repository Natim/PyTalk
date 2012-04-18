# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ConnectionDialog.ui'
#
# Created: Sun Jan 20 13:55:46 2008
#      by: PyQt4 UI code generator 4.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ConnectionDialog(object):
    def setupUi(self, ConnectionDialog):
        ConnectionDialog.setObjectName("ConnectionDialog")
        ConnectionDialog.resize(QtCore.QSize(QtCore.QRect(0,0,289,277).size()).expandedTo(ConnectionDialog.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(ConnectionDialog)
        self.vboxlayout.setObjectName("vboxlayout")

        self.groupBox = QtGui.QGroupBox(ConnectionDialog)
        self.groupBox.setObjectName("groupBox")

        self.gridlayout = QtGui.QGridLayout(self.groupBox)
        self.gridlayout.setObjectName("gridlayout")

        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label,0,0,1,1)

        self.userID = QtGui.QLineEdit(self.groupBox)
        self.userID.setObjectName("userID")
        self.gridlayout.addWidget(self.userID,0,1,1,1)

        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2,1,0,1,1)

        self.password = QtGui.QLineEdit(self.groupBox)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridlayout.addWidget(self.password,1,1,1,1)
        self.vboxlayout.addWidget(self.groupBox)

        self.groupBox_2 = QtGui.QGroupBox(ConnectionDialog)
        self.groupBox_2.setObjectName("groupBox_2")

        self.gridlayout1 = QtGui.QGridLayout(self.groupBox_2)
        self.gridlayout1.setObjectName("gridlayout1")

        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridlayout1.addWidget(self.label_3,0,0,1,1)

        self.server = QtGui.QLineEdit(self.groupBox_2)
        self.server.setObjectName("server")
        self.gridlayout1.addWidget(self.server,0,1,1,2)

        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridlayout1.addWidget(self.label_4,1,0,1,1)

        self.port = QtGui.QLineEdit(self.groupBox_2)
        self.port.setObjectName("port")
        self.gridlayout1.addWidget(self.port,1,1,1,1)

        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridlayout1.addWidget(self.label_5,2,0,1,1)

        self.ressource = QtGui.QLineEdit(self.groupBox_2)
        self.ressource.setObjectName("ressource")
        self.gridlayout1.addWidget(self.ressource,2,1,1,2)

        self.useSSL = QtGui.QCheckBox(self.groupBox_2)
        self.useSSL.setObjectName("useSSL")
        self.gridlayout1.addWidget(self.useSSL,1,2,1,1)
        self.vboxlayout.addWidget(self.groupBox_2)

        self.buttonBox = QtGui.QDialogButtonBox(ConnectionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.NoButton|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(ConnectionDialog)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),ConnectionDialog.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),ConnectionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConnectionDialog)

    def retranslateUi(self, ConnectionDialog):
        ConnectionDialog.setWindowTitle(QtGui.QApplication.translate("ConnectionDialog", "Connection Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ConnectionDialog", "Login\'s informations", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ConnectionDialog", "Jabber ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ConnectionDialog", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ConnectionDialog", "Server's informations", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ConnectionDialog", "Server:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ConnectionDialog", "Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ConnectionDialog", "Ressource:", None, QtGui.QApplication.UnicodeUTF8))
        self.ressource.setText(QtGui.QApplication.translate("ConnectionDialog", "PyTalk", None, QtGui.QApplication.UnicodeUTF8))
        self.useSSL.setText(QtGui.QApplication.translate("ConnectionDialog", "Using SSL", None, QtGui.QApplication.UnicodeUTF8))

