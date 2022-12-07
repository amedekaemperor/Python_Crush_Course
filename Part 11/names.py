from name_function import get_formatted_name

while True:
    first = input("First name: ")
    if first.lower() == 'quit':
        break
    last = input("Last name: ")
    if last.lower() == 'quit':
        break

    print(get_formatted_name(first, last))