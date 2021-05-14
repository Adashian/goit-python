USERS = dict()


def input_error(func):              # Функция обработчик ошибок
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            return 'User not found'
        except ValueError:
            return 'Not supported items'
        except IndexError:
            return 'Input name and number in space'
    return inner


@input_error
def add_contact(args):
    name = str(args[0]).title()
    num = args[1]
    USERS[name] = int(num)
    return f'Contact {name} was successfully added!'


@input_error
def change_contact(x):
    name = str(x[0]).title()
    num = x[1]
    USERS[name] = int(num)
    return f'Contact {name} was successfully changed. New number is {num}.'


@input_error
def show_phone(x):
    name = str(x[0]).title()
    return USERS.get(name, ['Name not found'])


def all_contacts(x):
    result = ''
    for name, phone in USERS.items():
        result += f'{name}: {phone}\n'
    return result


def hello(x):
    return 'How can I help you?'


commands = {
        'hello': hello,
        'add': add_contact,
        'change': change_contact,
        'phone': show_phone,
        'show all': all_contacts,
    }


def main():

    while True:
        user_input = input().casefold()
        if user_input == '.':
            break

        brake_commands = ['exit', 'close', 'good bye']
        if user_input in brake_commands:
            print('Good bye!')
            break

        splt_user_input = user_input.split()

        try:
            if splt_user_input[0] == 'show' and splt_user_input[1] == 'all':
                command = f'{splt_user_input[0]} {splt_user_input[1]}'
                splt_user_input.clear()
            else:
                command = splt_user_input.pop(0)
        except IndexError:
            print('Bad request.')
        try:
            handler = commands.get(command)(splt_user_input)
        except TypeError as error:
            print(error, 'Supporting next commands: add, hello, change, phone, show_all')
        else:
            print(handler)


if __name__ == '__main__':
    main()
