#!/usr/bin/env python
#flag_color.py
#Kamil Zukowski en Leon Graumans
#[teamoptimel]

import sys
from random import randrange
from PyQt4 import QtGui, QtCore

class FlagColor(QtGui.QWidget):

	def __init__(self):
		super(FlagColor, self).__init__()
		self.initUI()
	
	def initUI(self):
		
		self.col = QtGui.QColor(0, 0, 0)

		qbtn = QtGui.QPushButton('Random Color', self)
		qbtn.clicked.connect(self.buttonClicked)
		qbtn.resize(qbtn.sizeHint())
		qbtn.move(50, 20)
		
		self.square = QtGui.QFrame(self)
		self.square.setGeometry(5, 55, 200, 50)
		self.square.setStyleSheet("QWidget { background-color: %s }" %  
			self.col.name())       
        
		self.setGeometry(300, 300, 210, 110)
		self.setWindowTitle('FlagColor')    
		self.show()
	
	def buttonClicked(self):
		
		rcolor = randrange (1,4) 
		
		if rcolor
		
		#In case it is 1/2/3, we update the red/green/blue part of the color.
		if rcolor == 1:
			self.col.setRed(255)                
		elif rcolor == 2:
			self.col.setGreen(255)             
		else:
			self.col.setBlue(255) 
         
        #This style sheet changes the background color.   
		self.square.setStyleSheet("QFrame { background-color: %s }" %
			self.col.name())

def main():
	app = QtGui.QApplication(sys.argv)
	ex = FlagColor()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
