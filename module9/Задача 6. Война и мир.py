# Задача 6. «Война и мир»
# Что нужно сделать
# Мало кто не знает знаменитый роман Л. Н. Толстого «Война и мир». Это довольно объёмное произведение лежит в архиве
# voina-i-mir.zip. Напишите программу, которая подсчитывает статистику по буквам (не только русского алфавита) в этом
# романе и выводит результат на экран (или в файл). Результат должен быть отсортирован по частоте встречаемости букв
# (по возрастанию или убыванию). Регистр символов имеет значение.
#
# Архив можно распаковать вручную, но, если хотите, можете изучить документацию по модулю zipfile
# (можно использовать и другой модуль) и попробовать написать код, который будет распаковывать архив за вас.
# https://docs.python.org/3/library/zipfile.html

import zipfile


with zipfile.ZipFile('Ohlobystin_Musorshchik.zip', 'r') as myzip:
    myzip.extractall()

chars = {}
text_file = open('Ohlobystin_Musorshchik_RuLit_Me.txt', 'r', encoding='utf-8')

for line in text_file:
    for sym in line:
        if sym.isalpha():
            if sym in chars:
                chars[sym] += 1
            else:
                chars[sym] = 0

sorted_chars = sorted(chars.items(), reverse=True, key=lambda x: x[1])

for char_info in sorted_chars:
    print(char_info[0], char_info[1])
