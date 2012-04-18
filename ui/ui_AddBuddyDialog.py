# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_AddBuddyDialog.ui'
#
# Created: Thu Jan 24 17:11:47 2008
#      by: PyQt4 UI code generator 4.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AddBuddyDialog(object):
    def setupUi(self, AddBuddyDialog):
        AddBuddyDialog.setObjectName("AddBuddyDialog")
        AddBuddyDialog.resize(QtCore.QSize(QtCore.QRect(0,0,400,196).size()).expandedTo(AddBuddyDialog.minimumSizeHint()))
        AddBuddyDialog.setWindowIcon(QtGui.QIcon("images/im-jabber.png"))

        self.vboxlayout = QtGui.QVBoxLayout(AddBuddyDialog)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.label = QtGui.QLabel(AddBuddyDialog)
        self.label.setPixmap(QtGui.QPixmap("images/im-jabber.png"))
        self.label.setObjectName("label")
        self.hboxlayout.addWidget(self.label)

        self.label_2 = QtGui.QLabel(AddBuddyDialog)
        self.label_2.setObjectName("label_2")
        self.hboxlayout.addWidget(self.label_2)

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")

        self.label_3 = QtGui.QLabel(AddBuddyDialog)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3,0,0,1,1)

        self.jid = QtGui.QLineEdit(AddBuddyDialog)
        self.jid.setObjectName("jid")
        self.gridlayout.addWidget(self.jid,0,1,1,1)

        self.nicknameBouh = QtGui.QLabel(AddBuddyDialog)
        self.nicknameBouh.setObjectName("nicknameBouh")
        self.gridlayout.addWidget(self.nicknameBouh,1,0,1,1)

        self.nickname = QtGui.QLineEdit(AddBuddyDialog)
        self.nickname.setObjectName("nickname")
        self.gridlayout.addWidget(self.nickname,1,1,1,1)

        self.label_5 = QtGui.QLabel(AddBuddyDialog)
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.label_5,2,0,1,1)

        self.group = QtGui.QComboBox(AddBuddyDialog)
        self.group.setObjectName("group")
        self.gridlayout.addWidget(self.group,2,1,1,1)
        self.vboxlayout.addLayout(self.gridlayout)

        self.buttonBox = QtGui.QDialogButtonBox(AddBuddyDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.NoButton|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(AddBuddyDialog)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),AddBuddyDialog.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),AddBuddyDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddBuddyDialog)

    def retranslateUi(self, AddBuddyDialog):
        AddBuddyDialog.setWindowTitle(QtGui.QApplication.translate("AddBuddyDialog", "Add a new Buddy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddBuddyDialog", "Fill informations about you buddy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddBuddyDialog", "Jabber ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.nicknameBouh.setText(QtGui.QApplication.translate("AddBuddyDialog", "Nickname:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddBuddyDialog", "Group:", None, QtGui.QApplication.UnicodeUTF8))

