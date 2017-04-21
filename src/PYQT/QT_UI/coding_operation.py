import sys
from PyQt4 import QtGui , QtCore
from button import Ui_Form

class  MyForm(QtGui.QMainWindow):
	"""docstring for  MyForm"""
	def __init__(self, arg=None):
		super( MyForm, self).__init__()
		self.ui=Ui_Form()
		self.ui.setupUi(self)

if __name__=="__main__":
	app=QtGui.QApplication(sys.argv)
	myapp=MyForm()
	myapp.show()
	app.exec_()

