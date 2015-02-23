#!/usr/bin/env python
#flag_ui.py
#Kamil Zukowski en Leon Graumans
#[teamoptimel]

'''Niet gelukt om de random-kleur-functie te connecten met ComboBox'''

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
		'''Create UI'''
		self.col = QtGui.QColor(100, 255, 100)
		
		self.lbl = QtGui.QLabel("Welcome, choose a country", self)
		self.lbl.move (60,10)
		self.ComboBox = QtGui.QComboBox(self)
		newList = []
		for land in self.countries:
			newList.append(str(land))
		self.ComboBox.addItems(newList)
		self.ComboBox.activated[str].connect(self.updateUI)
		self.ComboBox.move(30,30)

		self.square = QtGui.QFrame(self)
		self.square.setGeometry(5, 75, 290, 170)
		self.square.setStyleSheet("QFrame { background-color: %s }" %
			self.col.name())
		#self.square.setStyleSheet("QFrame { background-color: %s }" %
		#	self.countries[self.ComboBox.currentIndex()].flag) 
		
	
		self.setGeometry(300, 300, 300, 250)
		self.setWindowTitle("Flagpicker")
		
		
		self.updateUI()

	def updateUI(self):
		'''Connect ComboBox with flagcolor'''
		self.square.setStyleSheet("QFrame { background-color: %s }" %
			self.col.name())
		#self.square.setStyleSheet("QFrame { background-color: %s }" %
		#	self.countries[self.ComboBox.currentIndex()].flag) 	
		
	
def main():
	
	app = QtGui.QApplication(sys.argv)
	form = FlagFrame()
	form.show()
	sys.exit(app.exec_())
	
	
if __name__ == "__main__":
	main()
