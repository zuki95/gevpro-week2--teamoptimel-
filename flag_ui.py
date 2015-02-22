#!/usr/bin/env python
#flag_ui.py

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class FlagFrame(QtGui.QWidget):
	
	def __init__(self):
		super(FlagFrame, self).__init__()

		self.initUI()
		
	def initUI(self):
		
		#self.countries = sorted(self.countries.keys())
		
		self.lbl = QtGui.QLabel("Welcome, choose a country.", self)
		data = self.getCountry()
		self.ComboBox = QtGui.QComboBox(self)
		self.ComboBox.addItems(self.countries)
		#self.ComboBox.activated[str].connect(self.onActivated)
		self.ComboBox.move(0,50)
	
		self.setGeometry(300, 300, 300, 200)
		self.setWindowTitle("Flagpicker")
		self.show()
		
	#def onActivated(self, text):
		
		#self.lbl.setText(text)
		#self.lbl.adjustSize()
		
		
	def getCountry(self):

		self.countries = []
		with open('countries_list.txt', 'r') as infile:
			for lines in infile:
				lines = lines.rstrip('\n')
				self.countries.append((lines))
	
	#def getCountry(self):
		
		#self.countries = []
		#with open('countries_list.txt', 'r') as infile:
			#for line in infile:
				#for countries in line.split():
					#return(countries)
	
def main():
	
	app = QtGui.QApplication(sys.argv)
	form = FlagFrame()
	sys.exit(app.exec_())
	
	
if __name__ == "__main__":
	main()
