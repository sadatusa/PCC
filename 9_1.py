# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating
# that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print('Restaurant '+self.restaurant_name,', cuisine '+self.cuisine_type)
    def open_restaurant(self):
        print(self.restaurant_name+' restaurant is open')

my_restaurant=Restaurant('Shahi Sahwari','Pakistani')

print(my_restaurant.restaurant_name,my_restaurant.cuisine_type)
print(my_restaurant.describe_restaurant())
print(my_restaurant.open_restaurant())

restaurant2=Restaurant('Chai Wala','Tea')

print(restaurant2.restaurant_name,restaurant2.cuisine_type)
print(restaurant2.describe_restaurant())
print(restaurant2.open_restaurant())