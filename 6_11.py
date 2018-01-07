# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information
# you have stored about it.

karachi={'Country':'Pakistan', 'Population':'10Mil', 'Fact':'lights'}
newyork={'Country':'USA', 'Population':'30Mil', 'Fact':'multi nations'}
zurich={'Country':'Switzerland', 'Population':'8Mil', 'Fact':'trams'}

cities={'Karachi':karachi,'Newyork':newyork,'Zurich':zurich}

for city,info in cities.items():
    print(city+': ',end='')
    for property,val in info.items():
        print(property+':'+val+', ',end='')
    print('')