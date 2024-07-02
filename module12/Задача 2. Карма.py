# Задача 2. Карма
# Что нужно сделать
# Один буддист-программист решил создать свой симулятор жизни, в котором нужно набрать 500 очков кармы (это константа),
# чтобы достичь просветления.
import random
# Каждый день вызывается специальная функция one_day(), которая возвращает количество кармы от 1 до 7 и может с
# вероятностью 1 к 10 выкинуть одно из исключений:

# KillError,
# DrunkError,
# CarCrashError,
# GluttonyError,
# DepressionError.
# (Исключения нужно создать самостоятельно, при помощи наследования от Exception.)

# Напишите такую программу. Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении кармы
# до уровня константы. Исключения обработайте и запишите в отдельный лог karma.log.

# По итогу у вас может быть примерно такая структура программы:
# открываем файл
# цикл по набору кармы
#    try
#       карма += one_day()
#    except(ы) с указанием классов исключений, которые нужно поймать
#       добавляем запись в файл
# закрываем файл

from pathlib import Path
import random


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


def one_day():
    if random.randint(1, 10) == 5:
        exceptions = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]
        random_exception = random.choice(exceptions)
        raise random_exception

    earned_karma_points = (random.randint(1, 7))
    return earned_karma_points


karma_points = 0
enlightenment_score = 500
with open(Path('karma.log'), 'w', encoding='utf-8') as karma_file:
    while True:
        try:
            if karma_points >= enlightenment_score:
                print('Вы достигли просветления!')
                break
            karma_points += one_day()
        except KillError:
            karma_file.write('Вас убили.\n')
        except DrunkError:
            karma_file.write('Отравились суррогатом.\n')
        except CarCrashError:
            karma_file.write('Автокатастрофа.\n')
        except GluttonyError:
            karma_file.write('Смерть от чревоугодия.\n')
        except DepressionError:
            karma_file.write('Суицид.\n')

# todo все ок, только сами сообщения можно было бы поместить внутрь эксепшена
# class MyException(Exception):
#     msg = "Some death reason"
# todo а потом ловить исключения скопом, и писать сообщение в файл
