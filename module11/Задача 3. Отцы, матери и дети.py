# Задача 3. Отцы, матери и дети
# Что нужно сделать:
# Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть:

# Имя,
# возраст,
# список детей.
# И он может:

# Сообщить информацию о себе,
# успокоить ребёнка,
# покормить ребёнка.
# У ребёнка есть:

# Имя,
# возраст (должен быть меньше возраста родителя хотя бы на 16 лет),
# состояние спокойствия,
# состояние голода.
# Реализация состояний — на ваше усмотрение. Это может быть и простой «флаг», и словарь состояний, и что-то поинтереснее

import random
from family import Parent # можно через запятую Parent, Child
from family import Child


def input_family_info():
    parent_name = input('Введите имя родителя: ')
    parent_age = int(input('Введите возраст родителя: '))
    all_children = []
    children_num = int(input('Введите кол-во детей: '))

    for _ in range(children_num):
        child_name = input('\nВведите имя ребенка: ')
        while True:
            child_age = int(input(f'Введите возраст {child_name}: '))
            if parent_age - child_age < 16:
                print('Разница между ребенком и родителем не должна быть меньше 16 лет!')
            else:
                break
        adding_child = Child(child_name, child_age, random.randint(0, 3), random.randint(0, 2))
        all_children.append(adding_child)

    return Parent(parent_name, parent_age, all_children), all_children


cur_parent, cur_children = input_family_info() # я бы вернул только parent, а детей потом получал через объект родителя и убрал приставки cur, i
print()
for i_child in cur_children:
    print(
        f'{i_child.name} {i_child.mind_states[i_child.mind_state]} и {i_child.hunger_states[i_child.hunger_state]}')
while True:
    action = int(input('\nУспокоить детей, введите "1"\n'
                       'Покормить детей, введите "2"\n'
                       'Показать информацию о родителе, введите "3"\n'
                       'Выйти из программы, введите "4"\n'))
    if action == 1:
        cur_parent.calm_down()
    elif action == 2:
        cur_parent.feed()
    elif action == 3:
        cur_parent.show_info()
    elif action == 4:
        break
    else:
        print('Ошибка Ввода!\n')
