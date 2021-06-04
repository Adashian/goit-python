import pickle
import re
from collections import UserList
from datetime import datetime


class AddressBook(UserList):
    data = []

    def add_record(self, data):
        self.data.append(data)

    def iterable(self, n=3):
        page = ''
        i = 0
        while i < n:
            page += next(self.data)
        yield page

    def find_contact(self, num):
        self.result = []
        for record in self.data:
            for number in record['Phones']:
                pattern = re.findall(num, number)
                if pattern:
                    self.result.append(record)
        return self.result


class Record:

    def __init__(self, name, phones=None, birthday=None):
        self.user_info = {
            'Name': name,
            'Phones': phones,
            'Birthday': birthday
        }


class Field:
    pass


class Name(Field):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Phone(Field):

    def __init__(self, phone):
        self.phones = list()
        try:
            validate = re.fullmatch('[+]\d{5,13}|\d{5,13}', phone)
            if validate:
                self.phones.append(phone)
            else:
                print(f'Expected number in format +ХХХХХХХХХХХ or ХХХХХХХХХХ and 5-13 digits')
        except:
            print('Bad request, expected string')

    def add_phone(self, phone):
        try:
            validate = re.fullmatch('[+]\d{5,13}|\d{5,13}', phone)
            if validate:
                self.phones.append(phone)
            else:
                print(f'Expected number in format +ХХХХХХХХХХХ or ХХХХХХХХХХ and 5-13 digits')
        except:
            print('Bad request, expected string')

    def __str__(self):
        return self.phones

    def del_phone(self, phone):
        self.phones.remove(phone)

    def change_phone(self, old_value, new_value):
        find_index = self.phones.index(old_value)
        try:
            validate = re.fullmatch('[+]\d{5,13}|\d{5,13}', phone)
            if validate:
                self.phones[find_index] = new_value
            else:
                print(f'Expected number in format +ХХХХХХХХХХХ or ХХХХХХХХХХ and 5-13 digits')
        except Exception:
            print('Bad request, expected string')


class Birthday(Field):

    def __init__(self, birthday):
        self.birthday = None
        try:
            self.birthday = datetime.strptime(birthday, '%d.%m.%Y')
        except Exception:
            print("Incorrect birthday format, expected day.month.year")

    def __repr__(self):
        if self.birthday:
            return self.birthday.strftime('%d.%m.%Y')
        return f'Birthday don\'t established'

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


book = AddressBook()
name = Name('Ivan')
phone = Phone('380981234567')
bd = Birthday('12.12.2002')
rec1 = Record(name, phone.phones, bd)
book.add_record(rec1.user_info)

name2 = Name('Valera')
phone2 = Phone('38098234567')
bd2 = Birthday('02.02.1992')
rec2 = Record(name2, phone2.phones, bd2)
book.add_record(rec2.user_info)

name3 = Name('Valera')
phone3 = Phone('3806398712355')
bd3 = Birthday('27.02.1998')
rec3 = Record(name3, phone3.phones, bd3)
book.add_record(rec3.user_info)

book.find_contact('123')

with open('test.txt', 'wb+') as file:
    pickle.dump(book, file)

with open('test.txt', 'rb+') as file:
    result = pickle.load(file)
    print(result)
