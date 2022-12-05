# Number Served: Start with your program from Exercise 9-1 (page 162). 
# Add an attribute called number_served with a default value of 0. 
# Create an instance called restaurant from this class. 
# Print the number of customers the restaurant has served, and 
# then change this value and print it again.
#  Add a method called set_number_served() that lets you set the number of 
#  customers that have been served. Call this method with a new number and 
#  print the value again.
# Add a method called increment_number_served() that lets you increment the 
# number of customers who’ve been served. Call this method with any number 
# you like that could represent how many customers were served in, say, 
# a day of business.

class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, inc):
        self.number_served += inc

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a a/an {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} opens at 8:00 pm.")

bambinees = Restaurant('Bambinees', 'Italian')

print(bambinees.number_served)

bambinees.number_served = 20
print(bambinees.number_served)

bambinees.set_number_served(40)
print(bambinees.number_served)

bambinees.increment_number_served(5)
print(bambinees.number_served)
    