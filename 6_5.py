# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

river_country={'nile':'egypt','moselle':'germany','pedieos':'cyprus'}
for river,country in river_country.items():
    print('The '+river.title()+' runs through '+country.title())
print()
for river in river_country.keys():
    print(river.title())
print()
for country in river_country.values():
    print(country.title())
