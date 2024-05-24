# Задача 1. Имена 2
# Что нужно сделать
# Есть файл people.txt, в котором построчно хранится N имён пользователей.

# Напишите программу, которая берёт количество символов в каждой строке файла и в качестве ответа выводит общую сумму.
# Если в какой-либо строке меньше трёх символов (не считая литерала \n), то вызывается ошибка и сообщение, в какой
# именно строке она возникла. Программа при этом не завершается и обрабатывает все имена файла.
# Также при желании можно вывести все ошибки в отдельный файл errors.log.

# Пример работы программы:

# Содержимое файла people.txt:
# Василий
# Николай
# Надежда
# Никита
# Ян
# Ольга
# Евгения
# Кристина

# Ответ в консоли:
# Ошибка: менее трёх символов в строке 5.
# Общее количество символов: 49.

def count_sym(file):
    total_sym = 0

    for i_line, line in enumerate(file):
        try:
            clear_line = line.rstrip()
            total_sym += len(clear_line)
            if len(clear_line) < 3:
                raise ValueError

        except ValueError:
            print(f'Ошибка: менее трёх символов в строке {i_line + 1}')

    return total_sym


with open('people.txt', 'r', encoding='utf-8') as people_file:
    print(f'Общее количество символов: {count_sym(people_file)}')
    