from collections import UserDict
from datetime import datetime


class AddressBook(UserDict):
    page_len = 5

    def add_record(self, key, values):
        self.data[Record.__name__] = key, values

    def __iter__(self):
        page = []
        for i in self.data:
            page.append(i)
            if self.page_len == len(page):
                yield page
                page = []
        if page:
            yield page


class Record:

    def __init__(self, name, phone=None, birthday=None):
        self.name = Name(name)
        self.phones = Phone().phones
        self.phones.append(phone)
        self.birthday = Birthday


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


class Phone(Field):

    def __init__(self):
        self.phones = []


class Birthday(Field):
    __birthday = None

    @property
    def birthday(self):
        try:
            return self.__birthday.strftime('%d.%m.%Y')
        except:
            print('Birthday don\'t established')

    @birthday.setter
    def birthday(self, birthday):
        try:
            self.__birthday = datetime.strptime(birthday, '%d.%m.%Y')
        except Exception:
            print("Incorrect format, expected day.month.year")
