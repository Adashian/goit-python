from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, key, values):
        self.data[Record.__name__] = key, values


class Record:

    def __init__(self, name, phone=None):
        self.name = Name(name)
        self.phones = Phone().phones
        self.phones.append(phone)

    def add_phone(self, phone):
        self.phones.append(phone)

    def del_phone(self, phone):
        self.phones.remove(phone)

    def change_phone(self, old_value, new_value):
        find_index = self.phones.index(old_value)
        self.phones[find_index] = new_value


class Field:
    pass


class Name(Field):

    def __init__(self, name):
        self.name = name


class Phone(Field):

    def __init__(self):
        self.phones = []



