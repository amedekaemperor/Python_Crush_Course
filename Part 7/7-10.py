# Dream Vacation: Write a program that polls users about their dream vacation. 
# Write a prompt similar to If you could visit one place in the world, where would you go? 
# Include a block of code that prints the results of the poll.

prompt = "If you could visit one place in the world, \
    \nwhere would you go? "

result = []
while True:
    location = input(prompt)
    if location.lower() == 'quit':
        break
    else:
        result.append(location)

print("\nHere are the resutls: ")
for item in result:
    print(item.title())