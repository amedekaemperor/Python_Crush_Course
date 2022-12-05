# Cars: Write a function that stores information about a car in a dictionary. 
# The function should always receive a manufacturer and a model name. 
# It should then accept an arbitrary number of keyword arguments. 
# Call the func- tion with the required information and 
# two other name-value pairs, such as a color or an optional feature.

def car_info(manufacturer, model_name, **args):
    args["manufactuere"] = manufacturer
    args["model number"] = model_name
    return args

car = car_info('Tesla', 'S plaid', color='black', optitional_feature='ludacris mode')
print(car)