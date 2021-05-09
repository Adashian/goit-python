# message = input("Введите сообщение: ")
# offset = int(input("Введите сдвиг: "))
# encoded_message = ""
# if offset > 26:
#     offset -= 26
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


message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
encoded_message = []
for ch in message:
    if ch.isupper():
        encoded_char = chr((ord(ch) + offset - 65) % 26 + 65)
    elif ch.islower():
        encoded_char = chr((ord(ch) + offset - 97) % 26 + 97)
    else:
        encoded_char = ch
    encoded_message.append(encoded_char)
print(''.join(encoded_message))


# from pprint import pprint
#
# with open('E:/dataset_3363_3.txt', 'r') as doc:
#     my_list = []
#     for line in doc:
#         line = line.strip()
#         my_list.append(line)
#     my_lower_list = [my_lower_list.lower() for my_lower_list in my_list]
# #    print(my_lower_list)
#
#     for i in my_list:
#         counter = my_lower_list.count(i)
#         print(i)