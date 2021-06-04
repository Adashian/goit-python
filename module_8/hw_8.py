from datetime import date, datetime, timedelta
from collections import defaultdict


def congratulate(users):
    day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    this_week = date.today().isocalendar().week  # От этой даты совершается проверка ДР на следующей недели
    result = defaultdict(list)

    for user in users:

        b_day = user.get('birthday')
        b_day_this_year = date(datetime.today().year, b_day.month, b_day.day)

        b_day_week = b_day_this_year.isocalendar().week
        b_day_week_day = b_day_this_year.isocalendar().weekday

        if this_week + 1 == b_day_week:
            day = day_names[b_day_week_day - 1]
            if b_day_week_day - 1 > 4:
                continue
            result[day].append(user.get('name'))

        if this_week == b_day_week and b_day_week_day - 1 > 4:
            day = day_names[0]
            result[day].append(user.get('name'))

    for key, values in result.items():
        print(f'{key}:', end=' ')
        print(*values, sep=', ')


test_data = [
    {'name': 'Andriy', 'birthday': date(1994, 5, 8)},
    {'name': 'Ivan', 'birthday': date(1992, 8, 5)},
    {'name': 'Georg', 'birthday': date(1995, 2, 12)},
    {'name': 'Yaroslav', 'birthday': date(1994, 8, 8)},
    {'name': 'Anton', 'birthday': date(1993, 10, 21)},
    {'name': 'Kirill', 'birthday': date(1992, 5, 14)},
    {'name': 'Alexandr', 'birthday': date(1995, 5, 8)},
    {'name': 'August', 'birthday': date(1994, 6, 27)}
]

congratulate(test_data)
