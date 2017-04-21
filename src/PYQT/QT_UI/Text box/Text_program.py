# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 10:35:04 2014

@author: rd64
"""
import sys
from text_read import Ui_Form
from PyQt4 import QtGui, QtCore

class StartUI(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.Button_read, QtCore.SIGNAL("clicked()"),self.file_dailog)

    def file_dialog(self):
        self.ui.text_window.setText("hello world , 你好吗？")





if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=StartUI()
    myapp.show()
    sys.exit(app.exec_())
