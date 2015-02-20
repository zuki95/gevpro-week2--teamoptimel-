def getCountry():

    with open('countries_list.txt', 'r') as infile:
        for line in infile:
            for country in line.split():
                print(country)


getCountry()
