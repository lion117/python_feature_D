# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 13:37:26 2014

@author: rd64
"""
from PyQt4 import QtGui
#from PyQt4 import QtCore

import sys
app=QtGui.QApplication(sys.argv)
widget=QtGui.QWidget()
widget.resize(300,200)
widget.setWindowTitle("hello world")


#button=widget.QPushButton("good !")
#app.connect(button,SIGNAL("clicked()"),app,SLOT("quit()"))

#button.show()
widget.show()
#app.connect(button,SIGNAL("clicked()"),app,SLOT("quit()"))
sys.exit(app.exec_())


