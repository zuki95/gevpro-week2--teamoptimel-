#!/usr/bin/env python
#flag_ui.py

import sys
from PyQt4 import QtGui, QtCore
import country
import flag_color


class FlagFrame(QtGui.QWidget):
	
	def __init__(self):
		super(FlagFrame, self).__init__()
		self.countries = country.getCountry()
		self.flag = flag_color.FlagColor()
		self.initUI()
		
	def initUI(self):
		
		self.col = QtGui.QColor(0, 0, 0)
		
		self.lbl = QtGui.QLabel("Welcome, choose a country", self)
		self.lbl.move (10,10)
		self.ComboBox = QtGui.QComboBox(self)
		newList = []
		for land in self.countries:
			newList.append(str(land))
		self.ComboBox.addItems(newList)
		self.ComboBox.currentIndexChanged.connect(self.updateUI)
		self.ComboBox.move(10,30)

		self.square = QtGui.QFrame(self)
		self.square.setGeometry(5, 55, 200, 50)
		self.square.setStyleSheet("QFrame { background-color: %s }" %
			self.col.name()) 
		
	
		self.setGeometry(300, 300, 300, 300)
		self.setWindowTitle("Flagpicker")
		self.show()
		
		self.updateUI()

	def updateUI(self):
		self.square.setStyleSheet("QFrame { background-color: %s }" %
			self.countries[self.ComboBox.currentIndex()].flag.country())	
		
	
def main():
	
	app = QtGui.QApplication(sys.argv)
	form = FlagFrame()
	sys.exit(app.exec_())
	
	
if __name__ == "__main__":
	main()
