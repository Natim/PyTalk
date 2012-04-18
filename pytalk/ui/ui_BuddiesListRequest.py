# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_BuddiesListRequest.ui'
#
# Created: Thu Jan 24 17:11:34 2008
#      by: PyQt4 UI code generator 4.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_BuddiesListRequest(object):
    def setupUi(self, BuddiesListRequest):
        BuddiesListRequest.setObjectName("BuddiesListRequest")
        BuddiesListRequest.resize(QtCore.QSize(QtCore.QRect(0,0,331,205).size()).expandedTo(BuddiesListRequest.minimumSizeHint()))
        BuddiesListRequest.setWindowIcon(QtGui.QIcon("images/im-jabber.png"))

        self.vboxlayout = QtGui.QVBoxLayout(BuddiesListRequest)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.label = QtGui.QLabel(BuddiesListRequest)
        self.label.setPixmap(QtGui.QPixmap("images/im-jabber.png"))
        self.label.setObjectName("label")
        self.hboxlayout.addWidget(self.label)

        self.jid = QtGui.QLabel(BuddiesListRequest)
        self.jid.setTextFormat(QtCore.Qt.AutoText)
        self.jid.setObjectName("jid")
        self.hboxlayout.addWidget(self.jid)

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)

        self.textEdit = QtGui.QTextEdit(BuddiesListRequest)
        self.textEdit.setObjectName("textEdit")
        self.hboxlayout1.addWidget(self.textEdit)
        self.vboxlayout.addLayout(self.hboxlayout1)

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")

        spacerItem2 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem2)

        self.pushButton = QtGui.QPushButton(BuddiesListRequest)
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.hboxlayout2.addWidget(self.pushButton)

        self.pushButton_2 = QtGui.QPushButton(BuddiesListRequest)
        self.pushButton_2.setObjectName("pushButton_2")
        self.hboxlayout2.addWidget(self.pushButton_2)
        self.vboxlayout.addLayout(self.hboxlayout2)

        self.retranslateUi(BuddiesListRequest)
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL("clicked()"),BuddiesListRequest.accept)
        QtCore.QObject.connect(self.pushButton_2,QtCore.SIGNAL("clicked()"),BuddiesListRequest.reject)
        QtCore.QMetaObject.connectSlotsByName(BuddiesListRequest)

    def retranslateUi(self, BuddiesListRequest):
        BuddiesListRequest.setWindowTitle(QtGui.QApplication.translate("BuddiesListRequest", "Buddies List Request", None, QtGui.QApplication.UnicodeUTF8))
        self.jid.setText(QtGui.QApplication.translate("BuddiesListRequest", "Buddies List request:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("BuddiesListRequest", "Accept", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("BuddiesListRequest", "Refuse", None, QtGui.QApplication.UnicodeUTF8))

