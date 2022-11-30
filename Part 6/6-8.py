# Pets: Make several dictionaries, where each dictionary represents a different pet. 
# In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets. Next, loop through your list and as you do, 
# print everything you know about each pet.

jack = {'kind': 'dog', 'owner': 'kevin'}
stacy = {'kind': 'cat', 'owner': 'angela'}
bond = {'kind': 'dog', 'owner': 'anya'}

pets = [jack, stacy, bond]

for pet in pets:
    print(pet)