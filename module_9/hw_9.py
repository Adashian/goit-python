users = {}


def add_contact(name, number):
    users[name] = int(number)


def change_contact(name, number):
    users[name] = number


def show_phone(name):
    return users.get(name, ['Name not found'])


def all_contacts():
    return users.items()


while True:
    command = input('How can I help you? \n').casefold()
    command = command.split()
    brake_command = ['.', 'exit', 'close', 'good bye']
    if command[0] in brake_command:
        print('Good bye!')
        break
    elif command == 'hello':
        print('How can I help you?')

    elif command[0] == 'add':
        try:
            add_contact(command[1], command[2])
        except IndexError:
            print('Give me name and phone please')
        except ValueError:
            print('Number must include only digits')
        else:
            print('Contact was successfully added')

    elif command[0] == 'change':
        try:
            change_contact(command[1], command[2])
        except ValueError:
            print('Number must include only digits')
        else:
            print('Contact was successfully changed')

    elif command[0] == 'phone':
        print(show_phone(command[1]))

    elif command[0] == 'show' and command[1] == 'all':
        print(*all_contacts())
