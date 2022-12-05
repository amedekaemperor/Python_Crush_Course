# Three Restaurants: Start with your class from Exercise 9-1. 
# Create three different instances from the class, and call describe_restaurant() 
# for each instance.

class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a a/an {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} opens at 8:00 pm.")

claires = Restaurant("Claires", "Sea food")
amys = Restaurant("Amy's", "Bakery")

claires.describe_restaurant()
amys.describe_restaurant()