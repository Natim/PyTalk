from PyQt4.QtGui import QDialog
from PyQt4.QtCore import SIGNAL

class MessageDialog(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        
