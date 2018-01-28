# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.

class User():
    def __init__(self, first_name, last_name,age,hight,color):
        self.first_name = first_name
        self.last_name = last_name
        self.age=age
        self.hight=hight
        self.color=color

    def describe_user(self):
        print(self.first_name, self.last_name,self.age,self.hight,self.color)
    def greet_user(self):
        print('Welcome '+self.first_name)

user_info = User('Sadat', 'Hussain',44,5.8,'white')
user2_info=User('Saleem', 'Khan',40,6.2,'pink')
print(user_info.describe_user())
print(user_info.greet_user())
print(user2_info.describe_user())
print(user2_info.greet_user())
