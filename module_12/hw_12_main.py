import pickle
from hw_12_cls import AddressBook, Record, Phone

USERS = AddressBook()


def input_error(func):
    '''Обработчик ошибок.'''
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
    '''Добавляет новый контакт.'''
    phone = Phone(args[1])
    print(phone)
    record = Record(str(args[0]).title())
    record.add_phone(phone)
    bd = input('Введи дату рождения в формате "день-месяц-год" или просто нажми Enter для пропуска...\n')
    if bd:
        while True:
            try:
                record.add_birthday(bd)
            except ValueError:
                bd = input('''Нужно ввести дату рождения в формате "01-01-2000", попробуй еще раз.
Если ты передумал добавлять дату, просто нажми Enter.\n''')
                if not bd:
                    break
            else:
                break
    USERS.add_record(record)
    return f'Contact {record} was successfully added!'


@input_error
def show_phone(x):
    '''Отображает информацию по контакту.'''
    name = str(x[0]).title()
    return USERS.get(name, ['Name not found'])


def all_contacts(n):
    '''Отображает все контакты.'''
    n = n[0] if n else 3
    print(f'Всего в книге {len(USERS)} контактов.')
    for name in USERS.iterable(n):
        print(*name)
        answer = input('Нажми Enter что бы продолжить или введите любой символ, что бы закончить просмотр.\n')
        if not answer:
            continue
        break


def hello(x):
    return 'How can I help you?'


def load_data(x):
    with open('test.pickle', 'rb') as f:
        global USERS
        USERS.update(pickle.load(f))


def save_data(x):
    with open('test.pickle', 'wb') as f:
        pickle.dump(USERS, f)


def find(value):
    print(value)
    result = USERS.find_contact(value[0])
    if not result:
        return 'Не найдено'
    pretty_view = ''
    for contact in result:
         pretty_view += contact + '\n'
    return pretty_view


def content(n):
    USERS.add_fake_records(100)


commands = {
    'hello': hello,
    'add': add_contact,
    'info': show_phone,
    'show all': all_contacts,
    'save': save_data,
    'load': load_data,
    'find': find,
    'content': content
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
            return 'Команда не распознана'
        try:
            handler = commands.get(command)(splt_user_input)
        except TypeError as error:
            print('Error: ', error)
        else:
            if handler:
                print(handler)


if __name__ == '__main__':
    main()
