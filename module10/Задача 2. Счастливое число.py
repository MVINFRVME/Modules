# Задача 2. Счастливое число
# Что нужно сделать
# Напишите программу, которая запрашивает у пользователя число до тех пор, пока сумма запрашиваемых чисел не станет
# больше либо равна 777. Каждое введённое число при этом дозаписывается в файл out_file.txt. Сделайте так, чтобы перед
# дозаписью программа с вероятностью 1 к 13 выдавала пользователю случайное исключение и завершалась.

# Пример 1
# Введите число: 10
# Введите число: 500
# Введите число: 200
# Введите число: 67
# Вы успешно выполнили условие для выхода из порочного цикла!
# Содержимое файла out_file.txt:
# 10
# 500
# 200
# 67

# Пример 2
# Введите число: 10
# Введите число: 500
# Вас постигла неудача!
# Содержимое файла out_file.txt:
# 10

import random


def try_to_escape(lucky_num, unlucky_num, file_name):
    user_summ = 0
    with open(file_name, 'a', encoding='utf-8') as record_file:
        try:
            while user_summ < lucky_num:
                num = int(input('Введите число: '))
                user_summ += num
                generated_num = random.randint(1, 13)
                if unlucky_num == generated_num:
                    raise ValueError
                record_num = f'{num} '
                record_file.write(record_num)

            else:
                print('Вы успешно выполнили условие для выхода из порочного цикла!')

        except ValueError:
            print('Вас постигла неудача!')


escape_num = 777
lose_num = 13
wr_file_name = 'out_file.txt'
try_to_escape(escape_num, lose_num, wr_file_name)
