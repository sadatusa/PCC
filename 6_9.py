# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places
# for each person. To make this exercise a bit more interesting, ask some friends
# to name a few of their favorite places. Loop through the dictionary, and print
# each person’s name and their favorite places.

aslam=['Karachi','Lahore','Islamabad']
jameel=['Newyork','Washington','Newjersey']
kamal=['Jeddah','Riyadh','Dammam']

favorite_places={'Aslam':aslam,'Jameel':jameel,'Kamal':kamal}

for name,favoriteplaces in favorite_places.items():
    print(name+' '+'favorite places are ',end='')
    for favoriteplace in favoriteplaces:
        print(favoriteplace+', ',end='')
    print('')