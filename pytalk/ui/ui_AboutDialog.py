# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_AboutDialog.ui'
#
# Created: Mon Jan 21 00:21:49 2008
#      by: PyQt4 UI code generator 4.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(QtCore.QSize(QtCore.QRect(0,0,360,231).size()).expandedTo(AboutDialog.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(AboutDialog)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.aboutIcon = QtGui.QLabel(AboutDialog)
        self.aboutIcon.setPixmap(QtGui.QPixmap("images/im-jabber.png"))
        self.aboutIcon.setObjectName("aboutIcon")
        self.hboxlayout.addWidget(self.aboutIcon)

        self.aboutTitle = QtGui.QLabel(AboutDialog)

        font = QtGui.QFont()
        font.setPointSize(24)
        font.setWeight(75)
        font.setBold(True)
        self.aboutTitle.setFont(font)
        self.aboutTitle.setTextFormat(QtCore.Qt.AutoText)
        self.aboutTitle.setObjectName("aboutTitle")
        self.hboxlayout.addWidget(self.aboutTitle)

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.aboutTextBrowser = QtGui.QTextBrowser(AboutDialog)
        self.aboutTextBrowser.setObjectName("aboutTextBrowser")
        self.vboxlayout.addWidget(self.aboutTextBrowser)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)

        self.closeButton = QtGui.QPushButton(AboutDialog)
        self.closeButton.setIcon(QtGui.QIcon("images/close.png"))
        self.closeButton.setObjectName("closeButton")
        self.hboxlayout1.addWidget(self.closeButton)
        self.vboxlayout.addLayout(self.hboxlayout1)

        self.retranslateUi(AboutDialog)
        QtCore.QObject.connect(self.closeButton,QtCore.SIGNAL("clicked()"),AboutDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QtGui.QApplication.translate("AboutDialog", "About PyTalk", None, QtGui.QApplication.UnicodeUTF8))
        self.aboutTitle.setText(QtGui.QApplication.translate("AboutDialog", "PyTalk 0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.aboutTextBrowser.setHtml(QtGui.QApplication.translate("AboutDialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PyTalk is a Jabber client in Python using PyQt4.</p>\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Programmed by Rémy Hubscher (c) 2008 for his Final Project at the University of Portsmouth</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("AboutDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

