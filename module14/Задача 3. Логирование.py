# Задача 3. Логирование
# Что нужно сделать
# Реализуйте декоратор logging, который будет отвечать за логирование функций. На экран выводится название функции и
# её документация. Если во время выполнения декорируемой функции возникла ошибка, то в файл function_errors.log
# записываются название функции и ошибки.

# Также постарайтесь сделать так, чтобы программа не завершалась после обнаружения первой же ошибки, а обрабатывала все
# декорируемые функции и сразу записывала все ошибки в файл.

# Дополнительно: запишите дату и время возникновения ошибки, используя модуль datetime.

# Что оценивается
# Результат вычислений корректен.
# Сообщения о процессе получения результата осмыслены и понятны для пользователя.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Классы и методы/функции имеют прописанную документацию.
# Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs).
# Если функция/метод ничего не возвращает, то используется None.
# Во всех декораторах используется functools.wraps().

from datetime import datetime
from functools import wraps
from pathlib import Path
from typing import Callable, List


def logging(func: Callable) -> Callable:
    """Декоратор logging, который отвечает за логирование функций. На экран выводится название функции и
    её документация. Если во время выполнения декорируемой функции возникла ошибка, то в файл function_errors.log
    записываются название функции и ошибки."""

    @wraps(func)
    def wrapped_func(*args, **kwargs):

        result = None
        print(f'\n-------------------------------\nИмя оборачиваемой функции: {func.__name__}\n\n'
              f'Документация:\n{func.__doc__}')
        try:
            result = func(*args, **kwargs)

        except Exception as exc:
            with open(Path('function_errors.log'), 'a', encoding='utf-8') as error_file:
                error_text = f'{datetime.now()}. Function name: "{func.__name__}" ; Error: "{str(exc)}"\n'
                error_file.write(error_text)
                print('Была вызвана ошибки, проверьте файл "function_errors.log"')

        return result

    return wrapped_func


@logging
def squares(n: int) -> List[int]:
    """Функция, которая возвращает список квадратов чисел в диапазоне от 1 до n.

    :param n: число, до которого будут генерироваться квадраты чисел (включительно).
    :type n: int

    :return square_seq: Возвращает список квадратов чисел
    :rtype square_seq: List[int]
    """
    square_seq = [elem ** 2 for elem in range(1, n + 1)]
    return square_seq


print(squares('asd'))
print(squares(12))

# ok
