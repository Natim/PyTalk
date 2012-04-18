from PyQt4.QtGui import QDialog
from PyQt4.QtCore import QSettings, QVariant, SIGNAL
from ui.ui_ConnectionDialog import Ui_ConnectionDialog

class ConnectionDialog(QDialog, Ui_ConnectionDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.connect(self, SIGNAL("accepted()"), self.saveSettings)
        self.readSettings()

    def readSettings(self):
        settings = QSettings("Trunat", "PyTalk")
        settings.beginGroup("Connection")
        self.userID.setText(settings.value("userID").toString())
        self.password.setText(settings.value("password").toString())
        self.server.setText(settings.value("server").toString())
        self.useSSL.setChecked(settings.value("useSSL", QVariant(True)).toBool())

        if self.useSSL.isChecked():
            self.port.setText(settings.value("port", QVariant("5223")).toString())
        else:
            self.port.setText(settings.value("port", QVariant("5222")).toString())

        self.ressource.setText(settings.value("ressource", QVariant("PyTalk")).toString())
        settings.endGroup()

    def saveSettings(self):
        settings = QSettings("Trunat", "PyTalk")
        settings.beginGroup("Connection")
        settings.setValue("userID", QVariant(self.userID.text()))
        settings.setValue("password", QVariant(self.password.text()))
        settings.setValue("server", QVariant(self.server.text()))
        settings.setValue("port", QVariant(int(self.port.text())))
        settings.setValue("ressource", QVariant(self.ressource.text()))
        settings.setValue("useSSL", QVariant(self.useSSL.isChecked()))
        settings.endGroup()
        self.emit(SIGNAL("configured()"))
