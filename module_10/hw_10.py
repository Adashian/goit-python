from collections import UserDict


class Field:

    def __init__(self):
        pass


class AddressBook(UserDict):

    def add_record(self, name, value):
        self.name = name
        self.value = value


class Record:

    def name(self):
        pass

    def value(self):
        pass


class Name:
    pass


class Phone:
    pass
