# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:30:07 2014

@author: rd64
"""

from PyQt4 import QtGui
from PyQt4 import QtCore
import sys


class ToolTip(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(500,500,300,200)
        self.setWindowTitle("tiptool")
        self.setToolTip("this is a <b>tooltip</b> widget")
        QtGui.QToolTip.setFont(QtGui.QFont("vender",20))

app=QtGui.QApplication(sys.argv)
tooptip=ToolTip()
tooptip.show()
app.exec_()

#class Tooltip(QtGui.QWidget):
#    def __init__(self, parent = None):
#        QtGui.QWidget.__init__(self, parent)
#        self.setGeometry(300, 300, 250, 150)
#        self.setWindowTitle('Tooltip')
#        self.setToolTip('This is a <b>QWidget</b> widget')
#        QtGui.QToolTip.setFont(QtGui.QFont('OldEnglish', 10))
#
#app = QtGui.QApplication(sys.argv)
#tooltip = Tooltip()
#tooltip.show()
#sys.exit(app.exec_())
