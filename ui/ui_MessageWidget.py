# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_MessageWidget.ui'
#
# Created: Tue Jan 22 07:03:54 2008
#      by: PyQt4 UI code generator 4.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MessageWidget(object):
    def setupUi(self, MessageWidget):
        MessageWidget.setObjectName("MessageWidget")
        MessageWidget.resize(QtCore.QSize(QtCore.QRect(0,0,400,300).size()).expandedTo(MessageWidget.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(MessageWidget)
        self.vboxlayout.setObjectName("vboxlayout")

        self.messageBrowser = QtGui.QTextBrowser(MessageWidget)
        self.messageBrowser.setObjectName("messageBrowser")
        self.vboxlayout.addWidget(self.messageBrowser)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)

        self.fontButton = QtGui.QPushButton(MessageWidget)
        self.fontButton.setIcon(QtGui.QIcon("images/font.png"))
        self.fontButton.setObjectName("fontButton")
        self.hboxlayout.addWidget(self.fontButton)

        self.videoButton = QtGui.QPushButton(MessageWidget)
        self.videoButton.setIcon(QtGui.QIcon("images/camera-web.png"))
        self.videoButton.setObjectName("videoButton")
        self.hboxlayout.addWidget(self.videoButton)

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.messageEdit = QtGui.QLineEdit(MessageWidget)
        self.messageEdit.setObjectName("messageEdit")
        self.hboxlayout1.addWidget(self.messageEdit)

        self.sendButton = QtGui.QPushButton(MessageWidget)
        self.sendButton.setIcon(QtGui.QIcon("images/send_mail.png"))
        self.sendButton.setObjectName("sendButton")
        self.hboxlayout1.addWidget(self.sendButton)
        self.vboxlayout.addLayout(self.hboxlayout1)

        self.retranslateUi(MessageWidget)
        QtCore.QMetaObject.connectSlotsByName(MessageWidget)

    def retranslateUi(self, MessageWidget):
        MessageWidget.setWindowTitle(QtGui.QApplication.translate("MessageWidget", "Message", None, QtGui.QApplication.UnicodeUTF8))
        self.messageBrowser.setHtml(QtGui.QApplication.translate("MessageWidget", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#00008b;\">[14:51] Mauryson :</span><span style=\" color:#00008b;\"> </span><span style=\" color:#000000;\">Salut</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><span style=\" font-weight:600; font-style:italic; color:#8b0000;\">[14:52] Natim :</span> Coucou</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.fontButton.setText(QtGui.QApplication.translate("MessageWidget", "&Font", None, QtGui.QApplication.UnicodeUTF8))
        self.videoButton.setText(QtGui.QApplication.translate("MessageWidget", "Video", None, QtGui.QApplication.UnicodeUTF8))
        self.sendButton.setText(QtGui.QApplication.translate("MessageWidget", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.sendButton.setShortcut(QtGui.QApplication.translate("MessageWidget", "Return", None, QtGui.QApplication.UnicodeUTF8))

