# Задача 2. Пути файлов
# Что нужно сделать
# Реализуйте функцию gen_files_path, которая рекурсивно проходит по всем каталогам (включая вложенные папки и подпапки)
# указанной директории (по умолчанию — корневой диск), находит указанный пользователем каталог и генерирует пути всех
# встреченных файлов.
#
# Подсказка: вместо написания кода с рекурсией используйте готовую рекурсивную функцию os.walk():
# os — Miscellaneous operating system interfaces — Python 3.11.0 documentation.
# (https://docs.python.org/3/library/os.html#os.walk)
#
# Что оценивается
# Результат вычислений корректен.
# Сообщения о процессе получения результата осмыслены и понятны для пользователя.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Классы и методы/функции имеют прописанную документацию.
# Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs). Если функция/метод ничего не
# возвращает, то используется None.


from os import walk
from pathlib import Path
from collections.abc import Iterable


def gen_files_path(searching_dir_name: str, directory: str = 'F:/') -> Iterable[Path]:
    """Функция генератор пути, которая рекурсивно проходит по всем каталогам указанной директории
    находит указанный пользователем каталог и генерирует пути всех встреченных файлов.

    :param searching_dir_name: Имя искомой директории
    :type searching_dir_name: str
    :param directory: Путь старта поиска(по умолчанию используется корневой диск)
    :type directory: str
    :return Path(cur_root, file): При помощи yield возвращает путь к файлу внутри искомой директории.
    :rtype: Iterable[Path]
    :rtype: Path
    """

    for root, dirs, files in walk(Path(directory)):
        for cur_dir in dirs:
            if cur_dir == searching_dir_name:
                print(f'\nНайдена искомая папка: {searching_dir_name}\nПуть к ней: {root}')
                target_path = Path(root, searching_dir_name)
                print(f'Файлы внутри искомой папки и путь к ним:')
                for cur_root, cur_dirs, cur_files in walk(target_path):
                    for file in cur_files:
                        yield Path(cur_root, file)


for path in gen_files_path('module3', 'F:/'):
    print(path)

# ok
