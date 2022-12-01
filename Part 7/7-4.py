# Pizza Toppings: Write a loop that prompts the user to enter a series 
# of pizza toppings until they enter a 'quit' value. As they enter each topping, 
# print a message saying you’ll add that topping to their pizza.

while True:
    topping = input("Enter topping: ")

    if topping.lower() == 'quit':
        break
    else:
        print(f"I will add {topping.title()} to your pizza.")

