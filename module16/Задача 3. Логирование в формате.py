# Задача 3. Логирование в формате
# Что нужно сделать
# Реализуйте декоратор, который будет логировать все методы декорируемого класса (кроме магических методов)
# и в который можно передавать формат вывода даты и времени логирования.
#
# Пример кода, передаётся формат «месяц день год — часы:минуты:секунды»:
#
# @log_methods("b d Y — H:M:S")
# class A:
#     def test_sum_1(self) -> int:
#         print('test sum 1')
#         number = 100
#         result = 0
#         for _ in range(number + 1):
#             result += sum([i_num ** 2 for i_num in range(10000)])
#
#         return result
#
# @log_methods("b d Y - H:M:S")
# class B(A):
#     def test_sum_1(self):
#         super().test_sum_1()
#         print("Наследник test sum 1")
#
#
#     def test_sum_2(self):
#         print("test sum 2")
#         number = 200
#         result = 0
#         for _ in range(number + 1):
#             result += sum([i_num ** 2 for i_num in range(10000)])
#
#         return result
#
# my_obj = B()
# my_obj.test_sum_1()
# my_obj.test_sum_2()
# Результат:
# Запускается 'B.test_sum_1'. Дата и время запуска: Apr 23 2021 — 21:50:37.
# Запускается 'A.test_sum_1'. Дата и время запуска: Apr 23 2021 — 21:50:37.
# Тут метод test_sum_1.
# Завершение 'A.test_sum_1', время работы = 0,187 s.
# Тут метод test_sum_1 у наследника.
# Завершение 'B.test_sum_1', время работы = 0,187 s.
# Запускается 'B.test_sum_2'. Дата и время запуска: Apr 23 2021 — 21:50:37.
# Тут метод test_sum_2 у наследника.
# Завершение 'B.test_sum_2', время работы = 0,370 s.
#
# Совет: внимательно пересмотрите видео 16.4 «Декораторы для классов», если сталкиваетесь с трудностями в этой задаче.
#
# Что оценивается в задаче
# Результат вычислений корректен.
# Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
# При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
# Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры с соответствующими декораторами.
# Для создания нового класса на основе уже существующего используется наследование.
# Для статических и классовых методов используется декоратор classmethod.
# Формат вывода соответствует примеру.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Классы и методы/функции имеют прописанную документацию.
# Есть аннотация типов для методов/функций и их аргументов, кроме args и kwargs. Если функция/метод ничего не возвращает
# , то используется None.

from datetime import datetime
from typing import Callable
import time, functools


def logging(cls, func: Callable, date_format: str) -> Callable:
    """Декоратор логирования для метода класса. Рассчитывает время работы функции и точное время запуска."""
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        new_date_format = ''
        for sym in date_format:  # изменяем формат даты из "b d Y — H:M:S" в "%b %d %Y — %H:%M:%S"
            if sym.isalpha():
                new_date_format += f'%{sym}'
            else:
                new_date_format += sym

        print(f'Запускается {cls.__name__}.{func.__name__}. '
              f'Дата и время запуска: {datetime.now().strftime(new_date_format)}')
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Завершение {cls.__name__}.{func.__name__}, время работы = {round(end_time - start_time, 3)} s')
        return  result
    return wrapped


def log_methods(format: str) -> Callable:
    """Декоратор для логирования класса."""
    def decorate_methods(cls):
        for method_name in dir(cls):
            if not method_name.startswith('__'):
                method = getattr(cls, method_name)
                if callable(method):
                    decorated_method = logging(cls, method, format)
                    setattr(cls, method_name, decorated_method)
        return cls
    return decorate_methods


@log_methods("b d Y — H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")


    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
