# Задача 5. Синглтон
# Что нужно сделать
# Синглтон — это порождающий паттерн проектирования, который гарантирует, что у класса есть только один экземпляр,
# и предоставляет к этому экземпляру глобальную точку доступа. Синглтонами мы уже пользовались, к ним относятся,
# например, None, True и False. Благодаря тому, что None — синглтон, можно использовать оператор is:
# он возвращает True только для объектов, представляющих одну и ту же сущность.
#
# Реализуйте декоратор singleton, который превращает класс в одноэлементный. При множественной инициализации
# объекта этого класса будет сохранён только первый инстанс, а все остальные попытки создания будут возвращать
# первый экземпляр.
#
# Пример кода:
#
# @singleton
# class Example:
#     pass
#
# my_obj = Example()
# my_another_obj = Example()
#
# print(id(my_obj))
# print(id(my_another_obj))
#
# print(my_obj is my_another_obj)
# Результат:
# 1986890616688
# 1986890616688
# True
#
# Что оценивается в задаче:
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Классы и методы/функции имеют прописанную документацию.
# Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs). Если функция или метод ничего
# не возвращает, то используется None.

import functools

def singleton(cls):
    """Декоратор класса. Превращает класс в синглтон (может иметь только один инстанс)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton

    wrapper_singleton.instance = None # кэш
    return wrapper_singleton


@singleton
class Example:
    pass

my_obj = Example()
my_another_obj = Example()
print(id(my_obj))
print(id(my_another_obj))
print(my_obj is my_another_obj)
