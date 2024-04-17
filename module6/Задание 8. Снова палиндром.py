# Задание 8. Снова палиндром
# Что нужно сделать
# Пользователь вводит строку. Необходимо написать программу, которая определяет, существует ли у этой строки
# перестановка, при которой она станет палиндромом. Затем она должна выводить соответствующее сообщение.
#
# Пример 1.
# Введите строку: aab
# Можно сделать палиндромом
#
# Пример 2.
# Введите строку: aabc
# Нельзя сделать палиндромом


text = input('Введите строку: ')
text_dict = dict()

for sym in text:
    if sym in text_dict:
        text_dict[sym] += 1
    else:
        text_dict[sym] = 1

odd_count = 0
for value in text_dict.values():
    if value % 2 != 0:
        odd_count += 1
if odd_count <= 1:
    print('Можно сделать палиндром')
else:
    print('Нельзя сделать палиндром')

# ok, хорошее решение

# или

# def is_palindrome(my_text):
#     text_dict = dict()
#     for sym in my_text:
#         text_dict[sym] = text_dict.get(sym, 0) + 1
#
#     odd_count = 0
#     for value in text_dict.values():
#         if value % 2 != 0:
#             odd_count += 1
#
#     return odd_count <= 1
#
#
# text = input('Введите строку: ')
# if is_palindrome(text):
#     print('Можно сделать палиндром!')
# else:
#     print('Нельзя сделать палиндром.')
