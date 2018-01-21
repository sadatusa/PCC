# 8-9. Magicians: Make a list of magician’s names. Pass the list to a function
# called show_magicians(), which prints the name of each magician in the list.

magicians_list=['kareem','jhons','michale']

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

show_magicians(magicians_list)

# 8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of magicians by adding
# the phrase the Great to each magician’s name. Call show_magicians() to
# see that the list has actually been modified.

def make_great(magicians):
    for x in range (0,len(magicians)):
        magicians[x]='The great '+magicians[x]

make_great(magicians_list)

print(magicians_list)