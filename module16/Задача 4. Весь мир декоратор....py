# Задача 4. Весь мир — декоратор…
# Что нужно сделать
# Реализуйте декоратор для декораторов: он должен декорировать другую функцию, которая должна быть декоратором,
# и даёт возможность любому декоратору принимать произвольные аргументы.
#
# Пример использования:
#
# @decorator_with_args_for_any_decorator
# def decorated_decorator(func: Callable, *args, **kwargs):... # отсюда уже сами!
#
# @decorated_decorator(100, 'рублей', 200, 'друзей')
# def decorated_function(text: str, num: int) -> None:
#     print("Привет", text, num)
#
# decorated_function("Юзер", 101)

# Результат:
# Переданные арги и кварги в декоратор: (100, 'рублей', 200, 'друзей') {}
# Привет, Юзер 101


# Что оценивается:
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Переменные, функции и собственные методы классов имеют значащие имена, не a, b, c, d.
# Классы и методы/функции имеют прописанную документацию.
# Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs). Если функция/метод ничего
# не возвращают, то используется None.

from typing import Callable
import functools

def decorator_with_args_for_any_decorator(decorator_to_enhance: Callable) -> Callable:
    """Декоратор. Дает возможность другому декоратору принимать произвольные аргументы"""
    def decorator_maker(*args, **kwargs) -> Callable:
        def decorator_wrapper(func: Callable) -> Callable:
            return decorator_to_enhance(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *dec_args, **dec_kwargs):
    """Декоратор. Шаблон"""
    @functools.wraps(func)
    def wrapper(*func_args, **func_kwargs) -> Callable:
        print(f'Переданные арги и кварги в декоратор: {dec_args} {dec_kwargs}')
        return func(*func_args, **func_kwargs)
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    """Пример декорируемой функции"""
    print("Привет", text, num)

decorated_function("Юзер", 101)
