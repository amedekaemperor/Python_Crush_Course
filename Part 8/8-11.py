# Archived Messages: Start with your work from Exercise 8-10. 
# Call the function send_messages() with a copy of the list of messages. 
# After calling the function, print both of your lists to show that the 
# original list has retained its messages

short_mgs = ['busy', 'call you later', 'good morning', 'hi']
sent_messages = []

def send_messages(arr):
    while arr:
        msg = arr.pop()
        print(msg)
        sent_messages.append(msg)

send_messages(short_mgs[:])

print(sent_messages)
print(short_mgs)