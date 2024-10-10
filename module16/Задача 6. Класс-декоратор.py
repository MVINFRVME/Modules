# Задача 6. Класс-декоратор
# Контекст
# Вы работаете в компании, которая разрабатывает программное обеспечение для финансовых анализов. Одна из ключевых
# задач в вашей работе — реализация сложного алгоритма для прогнозирования финансовых показателей. Этот алгоритм
# требует множества вычислений и может занимать длительное время.
#
# Вам поставлена задача создать декоратор, который будет логировать аргументы, результаты и время выполнения этой
# функции. Это поможет отслеживать прогресс выполнения алгоритма и анализировать его производительность.
#
# Задача:
# Создайте декоратор, который логирует аргументы, результаты и время выполнения функции.
# Реализуйте декоратор как класс и примените его к функции complex_algorithm. Запустите задекорированную функцию
# и проверьте время её выполнения.
# Замерить время выполнения кода можно при помощи модуля time:
#
# import time
# start_time = time.time() # Записываем время до вычислений
# # ...вычисления...
# end_time = time.time() # Затем записываем время после вычислений
# execution_time = end_time - start_time # Их разница будет временем выполнения кода вычислений
# Пример:
#
# @LoggerDecorator
# def complex_algorithm(arg1, arg2):
#     # Здесь выполняется “сложный” алгоритм
#     result = 0
#     for i in range(arg1):
#         for j in range(arg2):
#             with open('test.txt', 'w', encoding='utf8') as file:
#                 file.write(str(i + j))
#                 result += i + j
#     # Можете попробовать вынести создание файла из циклов и проверить, сколько времени алгоритм будет работать в этом случае
#     return result
#
# # Пример вызова функции с применением декоратора
# result = complex_algorithm(10, 50)
# Вывод в консоли:
#
# Вызов функции complex_algorithm
# Аргументы: (10, 50), {}
# Результат: 14500
# Время выполнения: 0.20143938064575195 секунд
# Советы
# Вспомните пример работы с классом-декоратором из видео «Декоратор как класс».
# Чтобы получить имя функции, используйте атрибут __name__: func.__name__


import time, functools
from typing import Callable


class LoggerDecorator:
    """Класс декоратор, который логирует аргументы, результаты и время выполнения функции"""
    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs) -> Callable:
        start_time = time.time()
        cur_result = self.func(*args, **kwargs)
        end_time = time.time()
        print(f'Вызов функции {self.func.__name__}\n'
              f'Аргументы: {args}, {kwargs}\n'
              f'Результат: {cur_result}\n'
              f'Время выполнения: {end_time - start_time}\n')
        return cur_result


@LoggerDecorator
def complex_algorithm(arg1, arg2):
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    return result


result = complex_algorithm(10, 50)
