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
		self.setColor()
	
	def initUI(self):
		
		self.col = QtGui.QColor(0, 0, 0)
   
	
	def setColor(self):
		'''Set random RGB value'''
		rc = randrange (1,256)
		self.col.setRed(rc)              
		self.col.setGreen(rc)
		self.col.setBlue(rc) 
		
		return self.col.name
         



