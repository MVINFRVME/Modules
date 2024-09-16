# Задача 4. Счётчик
# Что нужно сделать:
# Реализуйте декоратор counter, считающий и выводящий количество вызовов декорируемой функции.

# Для решения задачи нельзя использовать операторы global и nonlocal (об этом мы ещё расскажем).

# Что оценивается
# Результат вычислений корректен.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Классы и методы/функции имеют прописанную документацию.
# Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs). Если функция/метод ничего
# не возвращает, то используется None.
# Во всех декораторах используется functools.wraps().

from typing import Callable
from functools import wraps


def counter(func: Callable) -> Callable:
    """Декоратор, считающий и выводящий количество вызовов декорируемой функции."""
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapped_func.count += 1
        print(f'Функция "{func.__name__}" была вызвана {wrapped_func.count} раз(а). ')
        return result

    wrapped_func.count = 0
    return wrapped_func


@counter
def test(name: str) -> None:
    print(f'{name}, привет!')


test('Влад')
test('Илья')
test('Адольф')

# ok
