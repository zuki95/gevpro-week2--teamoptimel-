#!/usr/bin/env python
#flag_ui.py

import sys
from PyQt4 import QtGui, QtCore

class FlagFrame(QtGui.QWidget):
	
	def __init__(self):
		super(FlagFrame, self).__init__()
		
		self.initUI()
		
	def initUI(self):
		
		self.lbl = QtGui.QLabel("Country", self)
		data = self.getCountry()
		self.fromComboBox = QComboBox()
		self.fromComboBox.addItems(countries)
		
		self.fromComboBox.activated[str].connect(self.onActivated)
		
		self.setGeometry(300, 300, 300, 200)
		self.setWindowTitle("Flagpicker")
		self.show()
		
	def onActivated(self, text):
		
		self.lbl.setText(text)
		self.lbl.adjustSize()
		
		
	def getCountry(self):
		
		self.countries = []
		with open('countries_list.txt', 'r') as infile:
			for line in infile:
				for countries in line.split():
					return(countries)
					

	
		
		
def main():
	
	app = QtGui.QApplication(sys.argv)
	form = FlagFrame()
	form.show()
	app.exec_()
	
	
if __name__ == "__main__":
	main()
