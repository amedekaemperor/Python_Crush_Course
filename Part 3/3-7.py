# Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and now you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print a
# message to that person letting them know you’re sorry you can’t invite them
# to dinner.
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end of
# your program.

guests = ['thompson', 'hope', 'delanyo']

print(f"{guests.pop().title()} cannot make it.")

guests.append('selorm')

guests.insert(0, 'yola')
guests.insert(3, 'nordor')
guests.append('justice')

print("\nI'm sorry but I can only invite two people.")

while len(guests) > 2:
    print(f"I am very sorry {guests.pop().title()}, I can't invite you.")

for guest in guests:
    print(f"{guest.title()}, you're still invited.")

del guests[0: 2]

print(guests)
