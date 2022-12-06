# Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three 
# names of cats in the first file and three names of dogs in the second file. 
# Write a program that tries to read these files and print the contents of the 
# file to the screen. Wrap your code in a try-except block to catch the FileNotFound error, 
# and print a friendly message if a file is missing. Move one of the files to a dif- ferent 
# location on your system, and make sure the code in the except block executes properly.

from pathlib import Path

try:
    cats = Path("Part 10/cats.txt").read_text()
    dogs = Path("Part 10/dogs.txt").read_text()
except FileExistsError:
    print("File Not Found.")
else:
    print("Dogs: ")
    print(dogs)
    print("\nCats: ")
    print(cats)