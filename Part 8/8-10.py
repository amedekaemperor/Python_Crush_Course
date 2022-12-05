# Sending Messages: Start with a copy of your program from Exercise 8-9. 
# Write a function called send_messages() that prints each text message and 
# moves each message to a new list called sent_messages as it’s printed. 
# After calling the function, print both of your lists to make sure 
# the messages were moved correctly.

short_mgs = ['busy', 'call you later', 'good morning', 'hi']
sent_messages = []

def send_messages(arr):
    while arr:
        msg = arr.pop()
        print(msg)
        sent_messages.append(msg)

send_messages(short_mgs)

print(sent_messages)
print(short_mgs)