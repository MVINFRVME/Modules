# Задача 4. Турнир
# Что нужно сделать
# В файле first_tour.txt записано число K и данные об участниках турнира по настольной игре «Орлеан»: фамилии, имена и
# количество баллов, набранных в первом туре. Во второй тур проходят участники, которые набрали более K баллов в первом
# туре.

# Напишите программу, которая выводит в файл second_tour.txt данные всех участников, прошедших во второй тур,
# с нумерацией. В первой строке нужно вывести в файл second_tour.txt количество участников второго тура. Затем программа
# должна вывести фамилии, инициалы и количество баллов всех участников, прошедших во второй тур, с нумерацией. Имя нужно
# сократить до одной буквы. Список должен быть отсортирован по убыванию набранных баллов.

# Пример:
# Содержимое файла first_tour.txt:
# 80
# Ivanov Serg 80
# Sergeev Petr 92
# Petrov Vasiliy 98
# Vasiliev Maxim 78

# Содержимое файла second_tour.txt:
# 2
# 1) V. Petrov 98
# 2) P. Sergeev 92

import os


def eliminate_players(pass_score=None): # todo а зачем pass_score, если ты его потом берешь из файла?.
    # По сути не за чем, но Питон ругается, если не задать по умолчанию pass_score, "Local variable 'pass_score' might be referenced before assignment"
    # Что якобы мы можем сразу в else провалиться(хотя такого не может быть по сути) и там pass_score будет не инициализирован.

    # Понял, если дело в этом, то лучше прямо в теле функции добавить pass_score = None, хотя тут можно даже лучше
    # ты можешь считать отдельно первую строку через file.readline(), результат записать в переменную pass_score
    # а потом в цикле уже дочитать файл до конца
    players_passed = []
    file = open('first_tour.txt', 'r', encoding='utf-8')

    for i, line in enumerate(file):
        if i == 0:
            pass_score = int(line.rstrip())
        else:
            player = line.rstrip().split()
            points = int(player[2])
            if points > pass_score:
                players_passed.append(player)

    file.close()

    return players_passed


def document_sorted_winners(players):
    winners_file = open('second_tour.txt', 'w', encoding='utf-8') # todo тут кажется логичным использовать режим w для файла (а может и нет)
    amt_of_winners = len(players)                                 # если хочу перезаписать данные, то использую "w", если добавить , то "a".
    winners_file.write(str(amt_of_winners))                       # В рамках этой задача(при однократном запуске) мне кажется без разницы.
    sorted_players = sorted(players, reverse=True, key=lambda x: x[2])

    for player_num, players_info in enumerate(sorted_players):
        surname, first_name, score = players_info[0], players_info[1], players_info[2]
        first_surname_ch = first_name[:1]
        new_line = f'\n{player_num + 1}) {first_surname_ch}. {surname} {score}'
        winners_file.write(new_line)


winners = eliminate_players()
document_sorted_winners(winners)

# ok
