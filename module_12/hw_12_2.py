import pickle
import re
from collections import UserDict
from datetime import datetime


class AddressBook(UserDict):

    def __init__(self, file):
        super().__init__()
        self.__dict__ = self.deserialized_data()

    def add_record(self, record):
        self.data[record.name] = record.phones, record.birthday

    def __iter__(self):
        return iter(self.data)

    def find_contact(self, obj):
        self.result = []
        for key, value in self.data.items():
            if obj == key or obj in value:
                self.result.append(self.data[key])
        return self.result

    def deserialized_data(self):
        with open('test.txt', 'rb') as f:
            result = pickle.load(f)
        return result

    def serialized_data(self):
        with open('test.txt', 'wb') as f:
            pickle.dump(self, f)


class Record:

    def __init__(self, name, phone=None, birthday=None):
        self.name = name
        self.birthday = birthday
        self.phones = phone

    def days_to_birthday(self):
        if self.birthday:
            now_date = datetime.now()
            birthday_date = datetime.strptime(self.birthday, '%d.%m.%Y')
            delta1 = datetime(now_date.year, birthday_date.month, birthday_date.day)
            delta2 = datetime(now_date.year + 1, birthday_date.month, birthday_date.day)
            days = (max(delta1, delta2) - now_date).days + 1
            if days >= 365:
                return days - 365
            else:
                return days

    def __repr__(self):
        return f'{self.name}, {self.phones}, {self.birthday}'


class Field:
    pass


class Name(Field):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Phone(Field):

    def __init__(self, phone):
        self.__phones = []
        self.phone = phone

    @property
    def phone(self):
        return self.__phones

    @phone.setter
    def phone(self, value):
        try:
            treatment = (value.strip()
                         .replace('+', '')
                         .replace(')', '')
                         .replace('(', '')
                         .replace('-', '')
                         .replace(' ', '')
                         )
            validate = re.fullmatch('\\d{5,13}', treatment)
            if validate:
                self.__phones.append(treatment)
            else:
                print(f'Expected number in format +ХХХХХХХХХХХ or ХХХХХХХХХХ and 5-13 digits')
        except Exception as error:
            print(f'Bad request, expected string. {error}')

    def __repr__(self):
        return f'Numbers list - {self.__phones}'


class Birthday(Field):

    def __init__(self, birthday: str):
        self.__birthay = None
        self.birthday = birthday

    @property
    def birthday(self):
        return self.__birthay

    @birthday.setter
    def birthday(self, value):
        try:
            self.__birthday = datetime.strptime(value, '%d.%m.%Y')
        except Exception:
            print("Incorrect birthday format, expected day.month.year")

    def __repr__(self):
        return f'Birthday date - {self.__birthday}'


person = Name('Ivan')
phone = Phone('+380988910110')
birthday = Birthday('22.05.1992')
rec = Record(person, phone, birthday)
book = AddressBook()
book.add_record(rec)
