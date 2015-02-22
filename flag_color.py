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
   
	
	def setColor(self):
		
		rcolor = randrange (1,4)
		rc = randrange (1,256)
		
		self.col.setRed(rc)              
		self.col.setGreen(rc)
		self.col.setBlue(rc) 
         
        #This style sheet changes the background color.   
		#self.square.setStyleSheet("QFrame { background-color: %s }" %
			#self.col.name())


