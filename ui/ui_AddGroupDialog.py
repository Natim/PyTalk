# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_AddGroupDialog.ui'
#
# Created: Mon Jan 28 00:49:52 2008
#      by: PyQt4 UI code generator 4.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AddGroupDialog(object):
    def setupUi(self, AddGroupDialog):
        AddGroupDialog.setObjectName("AddGroupDialog")
        AddGroupDialog.resize(QtCore.QSize(QtCore.QRect(0,0,400,109).size()).expandedTo(AddGroupDialog.minimumSizeHint()))
        AddGroupDialog.setWindowIcon(QtGui.QIcon("images/im-jabber.png"))

        self.vboxlayout = QtGui.QVBoxLayout(AddGroupDialog)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.label = QtGui.QLabel(AddGroupDialog)
        self.label.setPixmap(QtGui.QPixmap("images/im-jabber.png"))
        self.label.setObjectName("label")
        self.hboxlayout.addWidget(self.label)

        self.label_2 = QtGui.QLabel(AddGroupDialog)
        self.label_2.setObjectName("label_2")
        self.hboxlayout.addWidget(self.label_2)

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.label_3 = QtGui.QLabel(AddGroupDialog)
        self.label_3.setObjectName("label_3")
        self.hboxlayout1.addWidget(self.label_3)

        self.group = QtGui.QLineEdit(AddGroupDialog)
        self.group.setObjectName("group")
        self.hboxlayout1.addWidget(self.group)
        self.vboxlayout.addLayout(self.hboxlayout1)

        self.buttonBox = QtGui.QDialogButtonBox(AddGroupDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.NoButton|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(AddGroupDialog)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),AddGroupDialog.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),AddGroupDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddGroupDialog)

    def retranslateUi(self, AddGroupDialog):
        AddGroupDialog.setWindowTitle(QtGui.QApplication.translate("AddGroupDialog", "Add a new group", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddGroupDialog", "Fill informations about your group:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddGroupDialog", "Group name:", None, QtGui.QApplication.UnicodeUTF8))

