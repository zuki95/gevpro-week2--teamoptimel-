#!/usr/bin/env python
#flag_color.py
#Kamil Zukowski en Leon Graumans
#[teamoptimel]

import sys
from random import randrange
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import kamilsshit


class FlagColor:
	def __init__(self, parent=QtGui.QColor):
		super(FlagColor, self).__init__(parent)

		landen = self.landen.keys()
		
		self.fromComboBox = QComboBox()
		self.fromComboBox.addItems(landen)



def main(argv):
	land = Country(argv[1])
	print(land.__str__())


if __name__ == '__main__':
	main(sys.argv)
