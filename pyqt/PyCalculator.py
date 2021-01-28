import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import PyCalculator_rcc
class Calculator(QDialog):
    def __init__(self, parent=None):
        super(Calculator,self).__init__(parent)
        self.browser = QTextBrowser()
        self.textF = QLineEdit("Enter something:")
        self.textF.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.textF)
        self.setLayout(layout)
        self.setWindowTitle('Py Calculator')
        self.textF.setFocus()
        self.textF.returnPressed.connect(self.updateUi)
        self.icon = QIcon(':/calculatorIcon.png')
        self.setWindowIcon(self.icon)
        self.trayIcon = QSystemTrayIcon(self.icon,self)
        self.trayIcon.show()
    def updateUi(self):
        try:
            s = self.textF.text()
            self.browser.append('%s = %s' % (s,eval(s)))
            self.textF.clear()
            
        except:
            self.browser.append('%s is invalid.' % s)
            self.trayIcon.showMessage('Py Calculator Error',
                '%s is invalid.' % s)
           
    
        
app = QApplication(sys.argv)
c = Calculator()
c.show()
app.exec_()
d = QSystemTrayIcon()
