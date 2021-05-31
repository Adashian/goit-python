from collections import UserDict
from datetime import datetime
import re


class AddressBook(UserDict):

    def add_record(self, key, values):
        self.data[key] = values
        Phone()._phones = []
        Birthday()._birthday = ''

    def iterable(self, n=3):
        page = ''
        i = 0
        while i < n:
            page += next(self.data)
        yield page


class Record:

    def __init__(self, name, phone=None, birthday=''):
        self.name = Name(name)
        self.phones = Phone()._phones
        if phone:
            self.phones.append(phone)
        self.birthday = Birthday()
        if birthday:
            self.birthday.set_birthday(birthday)

    def add_phone(self, phone):
        self.phones.append(phone)

    def del_phone(self, phone):
        self.phones.remove(phone)

    def change_phone(self, old_value, new_value):
        find_index = self.phones.index(old_value)
        self.phones[find_index] = new_value

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


class Field:
    pass


class Name(Field):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Phone(Field):
    _phones = list()

    @property
    def phones(self):
        return self._phones

    @phones.setter
    def phones(self, phone):
        try:
            validate = re.fullmatch('[+]\d{5,13}|\d{5,13}', phone)
            if validate:
                self._phones.append(phone)
            else:
                print(f'Expected number in format +ХХХХХХХХХХХ or ХХХХХХХХХХ and 5-13 digits')
        except:
            print('Bad request, expected string')


class Birthday(Field):
    _birthday = ''

    def set_birthday(self, birthday):
        try:
            self._birthday = datetime.strptime(birthday, '%d.%m.%Y')
        except Exception:
            print("Incorrect birthday format, expected day.month.year")

    def __repr__(self):
        if self._birthday:
            return self._birthday.strftime('%d.%m.%Y')
        return f'Birthday don\'t established'
