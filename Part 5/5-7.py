# Favorite Fruit: Make a list of your favorite fruits, 
# and then write a series of independent if statements that check for certain fruits in your list.
# • Make a list of your three favorite fruits and call it favorite_fruits.
# • Write five if statements. Each should check whether a certain kind of fruit is in your list. 
# If the fruit is in your list, the if block should print a statement, such as You really like bananas!

fruits = ['mango', 'orange', 'pineapple', 'banana']

fav_fruits = ['mango', 'pineapple']

for fruit in fav_fruits:
    if fruit in fruits:
        print(f"Your really like {fruit}.")