# Users: Make a class called User. Create two attributes called first_name and 
# last_name, and then create several other attributes that are typically stored in 
# a user profile. Make a method called describe_user() that prints a summary of the user’s information. 
# Make another method called greet_user() that prints a personalized greeting to the user.

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"This is {self.last_name.title()} {self.first_name.title()}.")

    def greet_user(self):
        print(f"Welcome, {self.last_name.title()} {self.first_name.title()}.")

user1 = User("emperor", "amedeka")

user1.greet_user()