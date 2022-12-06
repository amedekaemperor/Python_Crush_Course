# Read in each line from the file you just created, learning_python.txt, and 
# replace the word Python with the name of another language, such as C. 
# Print each modified line to the screen.

from pathlib import Path

contents = Path("Part 10/learning_python.txt").read_text()

for line in contents.splitlines():
    print(line.replace("Python", "C"))
