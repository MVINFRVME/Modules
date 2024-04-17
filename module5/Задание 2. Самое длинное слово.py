# Задание 2. Самое длинное слово
# Что нужно сделать
# Пользователь вводит строку, содержащую пробелы. Найдите в ней самое длинное слово, выведите его и его длину.
# Если таких слов несколько, выведите первое.
#
# Пример 1
#
# Введите строку: я есть строка
# Самое длинное слово: «строка»
# Длина этого слова: 6 символов
#
# Пример 2

# Введите строку: а б
# Самое длинное слово: «а»
# Длина этого слова: 1 символ
#
# Пример 3
#
# Введите строку: б
# Самое длинное слово: «б»
# Длина этого слова: 1 символ

# user_text = input('Введите строку: ')
#
# user_list = user_text.split(' ')
# the_longest_word = max(user_list, key=len)
# print(f'Самое длинное слово: {the_longest_word}'
#       f'\nДлинна этого слова: {len(the_longest_word)}')

# или

user_text = input('Введите строку: ')
user_list = user_text.split(' ')

max_count = 0
the_longest_word = None # так pycharm не будет ругаться

for word in user_list:
    if len(word) > max_count: # todo тут можно просто len взять
        max_count = len(word)
        the_longest_word = word

print(f'Самое длинное слово: {the_longest_word}'
      f'\nДлинна этого слова: {len(the_longest_word)}')

# ok
