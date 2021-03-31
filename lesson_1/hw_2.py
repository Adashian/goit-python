# ex_1
# is_next = None
# num = int(input("Введите количество баллов: "))
# if num >= 83:
#     is_next = True

# ex_2
# is_admin = False
# is_user = True
# is_permission = True
# access = None
# if is_admin or is_permission:
#     access = True
# else:
#     access = False

# ex_3
# work_experience = 4
#
# if 1 < work_experience <= 5:
#     developer_type = "Middle"
# elif work_experience <= 1:
#     developer_type = "Junior"
# else:
#     developer_type = "Senior"

# ex_4
# num = 99
#
# if 0 < num:
#     if num % 2 == 1:
#         result = "Положительное нечетное число"
#     else:
#         result = "Положительное четное число"
# elif 0 > num:
#     result = "Отрицательное число"
# else:
#     result = "Это ноль"

# ex_6
# num = int(input("Введите целое число (0 до 100): "))
# sum = 0
#
# while num != 0:
#     sum += num
#     num -= 1

# ex_7
# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = 0
# for symb in range(len(message)):
#     if search in message[symb]:
#         result += 1

# ex_9
# first = int ( input ( "Введите первое целое число: " ) )
# second = int ( input ( "Введите второе целое число: " ) )
#
# nod = max(first, second)
# while True:
#     if first % nod == 0 and second % nod == 0:
#         break
#     else:
#         nod -= 1

# ex_10
# while True:
#     num = int(input("Введите целое число (0 для выхода): "))
#     sum = 0
#     if num == 0:
#         break
#     for i in range(num + 1):
#         sum += i

# num = int(input("Введите целое число (0 для выхода): "))
# sum = 0
# while num != 0:
#     for i in range(num + 1):
#         sum += i
#     num = int(input("Введите целое число (0 для выхода): "))


# ex_11
# sum = 0
# while True:
#     num = int ( input ( "Введите целое число (0 для выхода): " ) )
#     if num == 0:
#         break
#
#     for i in range ( num + 1 ):
#         sum = sum + i

# ex_12
# sum = 0
# while True:
#     num = int(input("Введите целое число (0 для выхода): "))
#     if num == 0:
#         break
#     for i in range(num + 1):
#         if i % 2 != 0:
#             continue
#         sum = sum + i

# ex_13
# message = input("Введите сообщение: ")
# offset = int(input("Введите сдвиг: "))
# encoded_message = ""
# if offset > 26:
#     offset %= 26
# for ch in message:
#     if 64 < ord(ch) < 91:
#         if ord(ch) + offset > 90:
#             encoded_message += chr(ord(ch) + offset - 26)
#         else:
#             encoded_message += chr(ord(ch) + offset)
#     elif 96 < ord(ch) < 123:
#         if ord(ch) + offset > 122:
#             encoded_message += chr(ord(ch) + offset - 26)
#         else:
#             encoded_message += chr(ord(ch) + offset)
#     else:
#         encoded_message += ch
# print(encoded_message)

# ex_14
# pool = 1000
# quantity = 0
# try:
#     chunk = pool // quantity
# except ZeroDivisionError:
#     print('Выполнено деление на ноль!')

# ex_15
# result = None
# operand = None
# operator = None
# wait_for_number = False
# while True:
#     try:
#         first_operand = input()
#         first_operand = float(first_operand)
#     except ValueError:
#         print(f'{first_operand} is not a number. Try again.')
#     else:
#         result = first_operand
#         break
# while True:
#     while wait_for_number:
#         try:
#             operand = input('Введите число:\n')
#             operand = float(operand)
#         except ValueError:
#             print(f'{operand} is not a number. Try again.')
#         else:
#             wait_for_number = False
#     else:
#         if operator in ('+', '-', '*', '/'):
#             try:
#                 if operator == '+':
#                     result += operand
#                 elif operator == '-':
#                     result -= operand
#                 elif operator == '*':
#                     result *= operand
#                 elif operator == '/':
#                     result /= operand
#             except:
#                 wait_for_number = True
#                 continue
#         operator = input('Введите оператор:\n')
#         if operator in ('+', '-', '*', '/'):
#             wait_for_number = True
#         if operator in '=':
#             print(result)
#             break
#         elif operator not in ('+', '-', '*', '/'):
#             print(f'{operator} is not  +  or  -  or  /  or  * . Try again')
