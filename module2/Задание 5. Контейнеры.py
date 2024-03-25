# Задание 5. Контейнеры
# Что нужно сделать
# Контейнеры на складе лежат в ряд в порядке невозрастания (меньше либо равно) массы в килограммах.
# На склад привезли ещё один контейнер, который тоже нужно положить на определённое место.
# Напишите программу, которая получает на вход невозрастающую последовательность натуральных чисел.
# Они означают массу каждого контейнера в ряду. После этого вводится число X — масса нового контейнера.
# Программа выводит номер, под которым будет лежать новый контейнер.
# Если в ряду есть контейнеры с массой, как у нового, то его нужно положить после них.
#
# Обеспечьте контроль ввода: все числа не превышают 200.
#
# Пример:
#
# Количество контейнеров: 8
#
# Введите вес контейнера: 165
#
# Введите вес контейнера: 163
#
# Введите вес контейнера: 160
#
# Введите вес контейнера: 160
#
# Введите вес контейнера: 157
#
# Введите вес контейнера: 157
#
# Введите вес контейнера: 155
#
# Введите вес контейнера: 154
#
# Введите вес нового контейнера: 162
#
# Номер, который получит новый контейнер: 3

list_of_containers = []
number_of_containers = int(input('Количество контейнеров: '))

for container in range(number_of_containers):
    while True:
        container = int(input('Введите вес контейнера: '))
        if container <= 200: # не превышает это <=
            list_of_containers.append(container)
            break
        else:
            print('Контейнер не должен превышать 200 кг!')

new_container = int(input('Введите вес нового контейнера: '))
new_list = []

for index, value in enumerate(list_of_containers):
    if value < new_container:
        print(f'Номер, который получит новый контейнер: {index + 1}')
        break

# todo не учитывает условие, что если вес совпадает, то нужно положить после
# Количество контейнеров: 3
# Введите вес контейнера: 1
# Введите вес контейнера: 2
# Введите вес контейнера: 2
# Введите вес нового контейнера: 2
# Номер, который получит новый контейнер: 1

# Номер 4 ведь получит?
# Если в ряду есть контейнеры с массой, как у нового, то его нужно положить после них.
# И последовательность написано невозрастающая.
# Напишите программу, которая получает на вход невозрастающую последовательность натуральных чисел
#
# должен получить 4, но получает 1, я скопировал пример из консоли, попробуй воспроизвести.
