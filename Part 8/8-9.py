# Messages: Make a list containing a series of short text messages. 
# Pass the list to a function called show_messages(), which prints 
# each text message.

short_mgs = ['busy', 'call you later', 'good morning', 'hi']

def show_messages(arr):
    for msg in arr:
        print(msg)

show_messages(short_mgs)