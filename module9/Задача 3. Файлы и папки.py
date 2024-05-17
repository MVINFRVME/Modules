# Задача 3. Файлы и папки
# Что нужно сделать
# Напишите программу, которая получает на вход путь до каталога (в том числе это может быть просто корень диска) и
# выводит общее количество файлов и подкаталогов в нём. Также выведите на экран размер каталога в килобайтах
# (1 килобайт = 1024 байт).

# Важный момент: чтобы посчитать, сколько весит каталог, нужно найти сумму размеров всех вложенных в него файлов.

# Результат работы программы на примере python_basic\Module14:
# E:\PycharmProjects\python_basic\Module14
# Размер каталога (в Кбайтах): 8.373046875
# Количество подкаталогов: 7
# Количество файлов: 15

import os


def get_measures(cur_path):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if os.path.isfile(path):
            measures['size'] += os.path.getsize(path)
            measures['files'] += 1
        elif os.path.isdir(path):
            measures['dirs'] += 1
            get_measures(path)


measures = {'size': 0, 'files': 0, 'dirs': 0}
selected_path = os.path.abspath('..')
get_measures(selected_path)
converted_size = measures["size"] / 1024
print(f'{selected_path}\n'
      f'Размер каталога (в Кбайтах): {converted_size}\n'
      f'Количество подкаталогов: {measures["dirs"]}\n'
      f'Количество файлов: {measures["files"]}\n')
