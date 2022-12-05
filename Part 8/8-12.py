# Sandwiches: Write a function that accepts a list of items a person wants 
# on a sandwich. The function should have one parameter that collects as many 
# items as the function call provides, and it should print a summary of the 
# sandwich that’s being ordered. Call the function three times, using a 
# different num- ber of arguments each time.

def sandwich_toppings(*toppings):
    print("Making a sandwich with the following toppings: ")
    for topping in toppings:
        print(topping)

sandwich_toppings('cheese', 'mayonaise', 'ketchup')