# Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and 
# a medium shirt with the default message, and a shirt of any size with 
# a different message.

def make_shirt(text="I love Python", size="L"):
    print(f"Making a size-{size} t-shirt with the following text: {text}.")

make_shirt()
make_shirt("Say no", "S")