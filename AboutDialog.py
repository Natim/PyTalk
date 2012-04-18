from PyQt4.QtGui import *
from ui.ui_AboutDialog import Ui_AboutDialog

class AboutDialog(QDialog, Ui_AboutDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
