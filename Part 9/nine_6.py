# Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 
# Write a class called IceCreamStand that inherits from the Restaurant class 
# you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 166). 
# Either version of the class will work; just pick the one you like better. 
# Add an attribute called flavors that stores a list of ice cream flavors. 
# Write a method that displays these flavors. 
# Create an instance of IceCreamStand, and call this method.

class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a a/an {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} opens at 8:00 pm.")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['vanilla', 'chocolate', 'strawberry']

    def display_flavours(self):
        for flavour in self.flavours:
            print(flavour)
