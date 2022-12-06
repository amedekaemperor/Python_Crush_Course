#  User Dictionary: The remember_me.py example only stores one piece of information, the username. 
#  Expand this example by asking for two more pieces of information about the user, 
#  then store all the information you collect in a dictionary. 
#  Write this dictionary to a file using json.dumps(), and read it back in using json.loads(). 
#  Print a summary showing exactly what your program remembers about the user.

from pathlib import Path
import json

def user_profile(first, last, **args):
    args['first_name'] = first
    args['last_name'] = last
    Path("Part 10/profile.json").write_text(json.dumps(args))
    print(json.loads(Path("Part 10/profile.json").read_text()))

user_profile("Emperor", "Amedeka", prorammming_language = "Python")

