# Silent Cats and Dogs: Modify your except block in Exercise 10-7 to fail 
# silently if either file is missing.

from pathlib import Path

try:
    cats = Path("Part 10/cats.txt").read_text()
    dogs = Path("Part 10/dogs.txt").read_text()
except FileExistsError:
    pass
else:
    print("Dogs: ")
    print(dogs)
    print("\nCats: ")
    print(cats)