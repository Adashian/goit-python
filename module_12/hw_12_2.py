import pickle
import re
from collections import UserDict
from datetime import datetime


class AddressBook(UserDict):

    def __init__(self):
        super().__init__()
        self.num = 0

    def add_record(self, record):
        self.data[record.name] = record.phones, record.birthday
        self.serialized_data()

    def __iter__(self):
        return self

    def __next__(self):
        res = self.data.items()
        if self.num >= len(self.data):
            raise StopIteration

        self.num += 1
        return res

    def find_contact(self, obj: str):
        result = []
        for key, value in self.data.items():
            str_data = f'{key} {value}'
            if re.search(obj, str_data):
                result.append(str_data)
        return result

    def deserialized_data(self):
        with open('test.pickle', 'rb') as f:
            self.data = pickle.load(f)

    def serialized_data(self):
        with open('test.pickle', 'wb') as f:
            pickle.dump(self.data, f)


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
        self.__birthday = None
        self.birthday = birthday

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, value):
        try:
            self.__birthday = datetime.strptime(value, '%d.%m.%Y')
        except Exception:
            print("Incorrect birthday format, expected day.month.year")

    def __repr__(self):
        return f'Birthday date - {self.__birthday.date()}'


book = AddressBook()
