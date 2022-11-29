# No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct mes-
# sage is printed.

usernames = []

if usernames:
    print(f"{len(usernames)} are active.")
else:
    print("We need active users.")
