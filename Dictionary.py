#! /usr/bin/python

import sys
from PyQt4 import QtGui , QtCore
import lookup
import commands

class WinDict(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        
        cursor=QtGui.QCursor.pos()
        self.setGeometry(cursor.x()-150,20,500,500)
        self.setWindowTitle("Dabao Dictionary");
        self.setWindowFlags(QtCore.Qt.Popup)
        self.setBackgroundRole(19)

        grid=QtGui.QGridLayout()
        grid.setSpacing(10)        
        grid.addWidget(QtGui.QLabel("Word"), 1, 0)
        self.txtWord = QtGui.QLineEdit()
        self.txtRes = QtGui.QTextEdit()
        self.txtRes.setReadOnly(True)
        grid.addWidget(self.txtWord, 1, 1)
        grid.addWidget(self.txtRes, 3, 0, 5, 2)

        self.setLayout(grid)
        
        self.txtWord.returnPressed.connect(self.Translate)
        self.txtWord.setFocus()
            
    def Translate(self):
        res=lookup.look_up(self.txtWord.text())
        reload(sys)
        sys.setdefaultencoding('utf-8')
        res=unicode(res)
        self.txtRes.setText(res)
        #self.setWindowFlags(QtCore.Qt.Dialog)
        
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.txtWord.setText("")
            
    def hideEvent(self,event):
        print "Goodbye"
        quit()

app = QtGui.QApplication(sys.argv)
dict=WinDict()
reload(sys)
sys.setdefaultencoding('utf-8')
dict.show()
sys.exit(app.exec_())