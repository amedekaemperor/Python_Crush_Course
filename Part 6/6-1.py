# Person: Use a dictionary to store information about a person you know. 
# Store their first name, last name, age, and the city in which they live. 
# You should have keys such as first_name, last_name, age, and city. 
# Print each piece of information stored in your dictionary.

info = {
    'first_name': 'peter',
    'last_name': 'parker',
    'age': '22',
    'city': 'queens'
}

for key, value in info.items():
    print(f"{key}: {value}")

