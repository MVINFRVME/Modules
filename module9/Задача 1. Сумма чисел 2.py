# Задача 1. Сумма чисел 2
# Что нужно сделать
# Во входном файле numbers.txt записано N целых чисел, которые могут быть разделены пробелами и концами строк.
# Напишите программу, которая выводит сумму чисел во выходной файл answer.txt.

# Пример:
# Содержимое файла numbers.txt
#      2
# 2
#   2
#         2

# Содержимое файла answer.txt
# 8

# Основной функционал описан в отдельных функциях.
# Входные и выходные файлы названы так, как указано в задании.


def calculate_file_sum(cur_file, summ=0):
    numbers_file = open(cur_file, 'r')
    for line in numbers_file:
        clear_dig = int(line.strip())
        summ += clear_dig
    numbers_file.close()
    return summ


def write_answer(cur_file, summ):
    answer_file = open(cur_file, 'w')
    answer_file.write(str(summ))
    answer_file.close()


data_file_name = 'numbers.txt'
answer_file_name = 'answer.txt'
text_summ = calculate_file_sum(data_file_name)
write_answer(answer_file_name, text_summ)
