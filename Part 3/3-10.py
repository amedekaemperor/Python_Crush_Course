# Every Function: Think of things you could store in a list. For example, you
# could make a list of mountains, rivers, countries, cities, languages, or anything
# else you’d like. Write a program that creates a list containing these items and
# then uses each function introduced in this chapter at least once.

guests = ['thompson', 'hope', 'delanyo']

# append()
guests.append("duo")

#insert()
guests.insert(0, "jennifer")

# pop
guests.pop()

# remove()
guests.remove("hope")

# sort()
guests.sort()

# sorted()
sorted(guests)

print(guests)