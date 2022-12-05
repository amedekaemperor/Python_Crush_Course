# City Names: Write a function called city_country() that takes in 
# the name of a city and its country.

def city_country(city, country):
    return f"{city.title()}, {country.title()}"

print(city_country("new york", "USA"))