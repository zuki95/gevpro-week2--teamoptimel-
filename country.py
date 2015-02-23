#!/usr/bin/env python
#country.py
#Kamil Zukowski en Leon Graumans
#[teamoptimel]

import sys
import flag_color

class Country:
	'''Assign flag color to a country'''
	def __init__(self, country):
		self.country = country
		self.flag = flag_color.FlagColor()
	
	def __str__(self):
		return self.country
		#greet =  'Hello from' + ' ' + self.country +'.'
		#return greet
		
	def __repr__(self):
		return self.__str__()


def getCountry():
	'''Get data from countries_list file, append in new list'''
	countries = []
	with open('countries_list.txt', 'r') as infile:
		for lines in infile:
			lines = lines.rstrip('\n')
			countries.append(Country(lines))
	return countries
