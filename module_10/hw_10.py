from collections import UserDict


class AddressBook(UserDict):
    data = {}

    def __setitem__(self, key, item):
        self.data[Record] = key, item

    def __delitem__(self, key):
        del self.data[key]


class Record:
    records = dict()

    def add_contact(self, name, value=None):
        self.name = str(name).title()
        if value:
            self.num = value
            self.records[self.name] = int(self.num)

    def change_contact(self, name, new_number=None):
        self.name = str(name).title()
        self.num = new_number
        self.records[self.name] = int(self.num)

    def delete_contact(self, key):
        AddressBook().__delitem__(key)


class Field:
    pass


class Name(Field):

    def set_name(self, name):
        self.name = name


class Phone(Field):
    phones = []

    def set_phone(self, number):
        self.phones.append(number)
