# Задача 1. Права доступа
# Что нужно сделать
# Перед вами стоит задача создать и поддерживать специализированный форум. Вы только приступили и сейчас работаете
# над действиями, которые могут совершать посетители форума. Для разных пользователей прописаны разные возможности.
#
# Напишите декоратор check_permission, который проверяет, есть ли у пользователя доступ к вызываемой функции,
# и если нет, то выдаёт исключение PermissionError.
#
# Пример кода:
#
# user_permissions = ['admin']
#
# @check_permission('admin')
# def delete_site():
#     print('Удаляем сайт')
#
# @check_permission('user_1')
# def add_comment():
#     print('Добавляем комментарий')
#
# delete_site()
# add_comment()
# Результат:
# Удаляем сайт
# PermissionError: у пользователя недостаточно прав, чтобы выполнить функцию add_comment
#
# Что оценивается в задаче:
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Классы и методы (функции) имеют прописанную документацию.
# Есть аннотация типов для методов (функций) и их аргументов, кроме args и kwargs. Если функция или метод ничего
# не возвращает, то используется None.

from typing import Callable
import functools


def check_permission(name: str) -> Callable:
    """Декоратор, который проверяет, есть ли у пользователя доступ к вызываемой функции,
       если нет, то выдаёт исключение PermissionError."""
    def permission_decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if name not in user_permissions:
                raise PermissionError(f'у пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')
            result = func(*args, **kwargs)
            return result
        return wrapper
    return permission_decorator


user_permissions = ['admin']  # глобальная переменная

@check_permission('admin')
def delete_site() -> None:
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment() -> None:
    print('Добавляем комментарий')


try:
    delete_site()
    add_comment()
except PermissionError as exc:
    print(exc)
