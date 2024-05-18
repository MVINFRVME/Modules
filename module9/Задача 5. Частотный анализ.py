# Задача 5. Частотный анализ
# Что нужно сделать
# Есть файл text.txt, который содержит текст. Напишите программу, которая выполняет частотный анализ, определяя долю
# каждой буквы английского алфавита в общем количестве английских букв в тексте, и выводит результат в файл
# analysis.txt. Символы, не являющиеся буквами английского алфавита, учитывать не нужно.
#
# В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте, с тремя знаками в дробной части. Буквы должны
# быть отсортированы по убыванию их доли. Буквы с равной долей должны следовать в алфавитном порядке.
#
# Пример:
#
# Содержимое файла text.txt:
# Mama myla ramu.
#
# Содержимое файла analysis.txt:
# a 0.333
# m 0.333
# l 0.083
# r 0.083
# u 0.083
# y 0.083


def chars_in_text(name_of_file):
    text_file = open(name_of_file, 'r', encoding='utf-8')
    all_chars = {}
    chars_count = 0

    for char in text_file.read().lower():
        if char.isalpha():
            if char in all_chars:
                chars_count += 1
                all_chars[char] += 1
            else:
                chars_count += 1
                all_chars[char] = 1

    text_file.close()
    return all_chars, chars_count


def write_sorted_percentage_of_chars(chrs, total_chrs, name_of_file): # todo передал сюда значение, но не использовал его
    analysis_file = open(name_of_file, 'w', encoding='utf-8')

    for char, count in chars.items():
        proportion = round(count / total_chars, 3) # todo тут total_chars из 59 строки, а не то, которое ты в функцию передал
        chars[char] = proportion
    sorted_chars = sorted(chrs.items(), key=lambda x: (-x[1], x[0])) # todo с chars и chrs тоже самое, внутри функции нужно работать с переменными функции или
    # todo константами, иначе можно получить ошибку, которую потом будет трудно отловить

    for i_line in sorted_chars:
        line = f'{i_line[0]} {i_line[1]}\n'
        analysis_file.write(line)

    analysis_file.close()


file_name = 'text.txt'
rec_file_name = 'analysis.txt'
chars, total_chars = chars_in_text(file_name)
write_sorted_percentage_of_chars(chars, total_chars, rec_file_name)


