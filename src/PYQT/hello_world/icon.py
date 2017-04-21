# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:07:28 2014

@author: rd64
"""

from PyQt4 import QtGui
import sys
#
class Icon(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300,400,300,200)
        self.setWindowTitle("Icon")
        self.setWindowIcon(QtGui.QIcon('D:\code text\python\PYQT\hello_world/smile.ico'))

app=QtGui.QApplication(sys.argv)
icon=Icon()
icon.show()
app.exec_()

#there result cannot get what i need .no change had happened

# there reason why the function could not work is because the function i had entered is incorrect . and the rule of python it seems i had forgot .

#import sys
#from PyQt4 import QtGui
#class Icon(QtGui.QWidget):
#    def __init__(self, parent = None):
#        QtGui.QWidget.__init__(self, parent)
#        self.setGeometry(300, 300, 250, 150)
#        self.setWindowTitle('Icon')
#        self.setWindowIcon(QtGui.QIcon('hello_world/smile.ico'))
#
#app = QtGui.QApplication(sys.argv)
#icon = Icon()
#icon.show()
#sys.exit(app.exec_())




