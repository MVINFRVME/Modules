# Задача 2. Функция обратного вызова
# Что нужно сделать
# При работе с сетью и веб-сервисами иногда используется функция callback, так называемая функция обратного
# вызова. Это функция, которая вызывается при срабатывании определённого события: переходе на страницу,
# получении сообщения или окончании обработки процессором. В неё можно передать функцию, чтобы она выполнилась
# после определённого события. Это используется, например, в HTTP-серверах в ответ на URL-запросы. Реализуйте
# такую функцию.
#
# Пример функции:
#
# @callback('//')
# def example():
#     print('Пример функции, которая возвращает ответ сервера')
#     return 'OK'
#
# Основной код:
# route = app.get('//')
# if route:
#     response = route()
#     print('Ответ:', response)
# else:
#     print('Такого пути нет')
# Ожидаемый результат: пример функции, которая возвращает ответ сервера.
# Ответ: OK.
#
# Подсказка: функция callback, в зависимости от условия, может быть вызвана следующим действием или просто так.
#
# Что оценивается в задаче
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Классы и методы (функции) имеют прописанную документацию.
# Есть аннотация типов для методов (функций) и их аргументов, кроме args и kwargs. Если функция или метод ничего
# не возвращает, то используется None.

import functools
from typing import Callable

app = {}

def callback(route: str) -> Callable:
    """Декоратор функции обратного вызова."""
    def callback_decorator(func: Callable) -> Callable:
        app[route] = func
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result =  func(*args, **kwargs)
            return result
        return wrapper
    return callback_decorator


@callback('//')
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')