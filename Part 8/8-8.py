# User Albums: Start with your program from Exercise 8-7. 
# Write a while loop that allows users to enter an album’s artist and title. 
# Once you have that information, call make_album() with the user’s input and 
# print the dictionary that’s created. Be sure to include a quit value in 
# the while loop.

def make_album(artist_name, album_title, song_number=None):
    return {'Artist name': artist_name,
            'Album title': album_title,
            'Number of songs': song_number
    }

running = True
while running:
    name = input("Artist name: ")
    title = input("Album title: ")
    number = input("Number of songs: ")
    running = False

print(make_album(name, title))