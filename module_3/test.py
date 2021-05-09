def get_fullname(first_name, last_name, middle_name=''):
    x = ''
    if middle_name:
        x = first_name + ' ' + middle_name + ' ' + last_name
        return x
    x = first_name + ' ' + last_name
    return x

print(get_fullname('Anton', 'Kalash'))