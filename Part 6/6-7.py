# People: Start with the program you wrote for Exercise 6-1 (page 98). 
# Make two new dictionaries representing different people, 
# and store all three dictionar- ies in a list called people. 
# Loop through your list of people. As you loop through the list, 
# print everything you know about each person.

user_0 = {
    'first_name': 'peter',
    'last_name': 'parker',
    'age': 22,
    'city': 'queens'
}

user_1 = {
    'first_name': 'mary',
    'last_name': 'jane',
    'age': 20,
    'city': 'queens'
}

user_2 = {
    'first_name': 'aunt',
    'last_name': 'may',
    'age': 65,
    'city': 'queens'
}

people = [user_0, user_1, user_2]

for person in people:
    print(person)