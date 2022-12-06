# Favorite Number Remembered: Combine the two programs you wrote in Exercise 10-11 
# into one file. If the number is already stored, report the favorite number to the user. 
# If not, prompt for the user’s favorite number and store it in a file. 
# Run the program twice to see that it works.

from pathlib import Path
import json
import ten_11

if bool(Path("Part 10/fav_number.json").read_text()) == True:
    ten_11.read_fav_num()
else:
    ten_11.store_fav_num()
    ten_11.read_fav_num()