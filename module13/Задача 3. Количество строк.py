# Задача 3. Количество строк
# Что нужно сделать
# Реализуйте функцию-генератор, которая берёт все питоновские файлы в директории и вычисляет количество строк в каждом
# файле, игнорируя пустые строки и строки комментариев. По итогу функция-генератор должна с помощью yield каждый раз
# возвращать количество строк в очередном файле.
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Сообщения о процессе получения результата осмыслены и понятны для пользователя.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Классы и методы/функции имеют прописанную документацию
# Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs). Если функция/метод ничего не
# возвращает, то используется None.


from pathlib import Path
from collections.abc import Iterable


def count_lines_generator(cur_path: str) -> Iterable[int]:
    """Функция-генератор берёт все файлы с расширением ".py" в директории и вычисляет количество строк в каждом
     файле, игнорируя пустые строки и строки комментариев.


     :param cur_path: Путь к директории
     :type cur_path: str
     :return count_lines: С помощью yield каждый раз возвращает количество строк в очередном файле
     :rtype: Iterable[int]
     :return count_lines: С помощью yield каждый раз возвращает количество строк в очередном файле.
     :rtype: Generator[int]
     """
    py_files = list(Path(cur_path).glob('*.py'))
    for file in py_files:
        count_lines = 0
        with open(file, 'r', encoding='utf-8') as cur_file:
            for line in cur_file:
                stripped_line = line.strip()
                if (stripped_line != '') and (not stripped_line.startswith('#')):
                    count_lines += 1
            yield count_lines


path_to_directory = '/Modules/module10'
for file_num, line_count in enumerate(count_lines_generator(path_to_directory)):
    print(f'Файл {file_num + 1}: {line_count} строк.')
