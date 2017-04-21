# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:56:14 2014

@author: rd64
"""
from PyQt4 import QtGui, QtCore
import sys

#class QButton(QtGui.QWidget):
#	def __init__ (self, parent = None):
#		QtGui.QWidget.__init__(self, parent)
#		self.setGoemetry(300,300,300,200)
#       	self.setWindowTitle('quitbutton')
#		quit = QtGui.QPushButton('Close', self)
##		quit =QtGui.QPushButton('close',self)  #get the object from the parents object
#        quit.setGoemetry(20,20,30,20)
##	  	 self.connect(Bclose, QtCore.SIGNAL("clicked()"),
##                  QtGui.qApp , QtCore.SLOT("quit()"))
#        self.connect(quit, QtCore.SIGNAL('clicked()'), QtGui.qApp,
#                 QtCore.SLOT('quit()'))


class QuitButton(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('quitbutton')

        quit = QtGui.QPushButton('Close', self)
        quit.setGeometry(10, 10, 60, 35)
        self.connect(quit, QtCore.SIGNAL('clicked()'), QtGui.qApp ,
                 QtCore.SLOT('quit()'))


app=QtGui.QApplication(sys.argv)
button=QuitButton()
button.show()
app.exec_()

