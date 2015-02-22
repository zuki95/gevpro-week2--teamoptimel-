def getCountry():

	with open('countries_list.txt', 'r') as infile:
		for line in infile:
			line = line.rstrip('\n') #haalt newlines onder elke line weg
			print (line) #heb 'm zo gelaten, als je de line nog gaat strippen haalt ie landen United States ook uit elkaar
           # for country in line.strip():
                #print(country)

getCountry()
