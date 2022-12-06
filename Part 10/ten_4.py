# Guest: Write a program that prompts the user for their name. 
# When they respond, write their name to a file called guest.txt.

from pathlib import Path

running = True
names = ''

while running:
    name = input("Enter name: ")
    if name.lower() != 'quit':
        names += f"{name}\n"
    else: 
        running = False

Path("Part 10/guests.txt").write_text(names)
