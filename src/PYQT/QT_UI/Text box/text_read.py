# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'text_read.ui'
#
# Created: Thu Jan 16 14:00:19 2014
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(568, 378)
        self.Button_read = QtGui.QPushButton(Form)
        self.Button_read.setGeometry(QtCore.QRect(20, 20, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Button_read.setFont(font)
        self.Button_read.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../hello_world/smile.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_read.setIcon(icon)
        self.Button_read.setIconSize(QtCore.QSize(32, 32))
        self.Button_read.setAutoDefault(False)
        self.Button_read.setDefault(False)
        self.Button_read.setFlat(False)
        self.Button_read.setObjectName(_fromUtf8("Button_read"))
        self.Button_save = QtGui.QPushButton(Form)
        self.Button_save.setGeometry(QtCore.QRect(200, 20, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Button_save.setFont(font)
        self.Button_save.setObjectName(_fromUtf8("Button_save"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 20, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.text_window = QtGui.QTextEdit(Form)
        self.text_window.setGeometry(QtCore.QRect(20, 90, 521, 261))
        self.text_window.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.text_window.setObjectName(_fromUtf8("text_window"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.hide)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_read.setText(QtGui.QApplication.translate("Form", "read", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_save.setText(QtGui.QApplication.translate("Form", "save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form", "hide", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

