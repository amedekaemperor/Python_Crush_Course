# Favorite Number: Write a program that prompts for the user’s favorite number. 
# Use json.dumps() to store this number in a file. Write a separate program that 
# reads in this value and prints the message “I know your favorite number! 
# It’s _____.”

from pathlib import Path
import json

# function to store favorite number in json format
def store_fav_num():
    fav_number = json.dumps(input("Enter favorite number: "))
    Path("Part 10/fav_number.json").write_text(fav_number)

# function to read favorite number from json file
def read_fav_num():
    file = Path("Part 10/fav_number.json").read_text()
    fav_number = json.loads(file)
    print(f"I know your favorite number!\nIt's {fav_number}.")


