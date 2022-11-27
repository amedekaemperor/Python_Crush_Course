# More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.

# Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
# end of your program, informing people that you found a bigger table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

guests = ['thompson', 'hope', 'delanyo']

print(f"{guests.pop().title()} cannot make it.")

guests.append('selorm')

print("I found a bigger table.")

guests.insert(0, 'yola')
guests.insert(3, 'nordor')
guests.append('justice')

print("\n")

for guest in guests:
    print(f"{guest.title()}, I invite you to my family dinner.")

