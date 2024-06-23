# Задача 5. Совместное проживание

# Что нужно сделать:
# Чтобы понять, стоит ли ему жить с кем-то или лучше остаться в гордом одиночестве, Артём решил провести необычное
# исследование. Для этого он реализовал модель человека и модель дома.
#
# Человек может (должны быть такие методы):
#
# есть (+ сытость, − еда);
# работать (− сытость, + деньги);
# играть (− сытость);
# ходить в магазин за едой (+ еда, − деньги);
# прожить один день (выбирает одно действие согласно описанному ниже приоритету и выполняет его).
# У человека есть (должны быть такие атрибуты):
#
# имя,
# степень сытости (изначально 50),
# дом.
# В доме есть:
#
# холодильник с едой (изначально 50 еды),
# тумбочка с деньгами (изначально 0 денег).
# Если сытость человека становится меньше нуля, человек умирает.
#
# Логика действий человека определяется следующим образом:
#
# Генерируется число кубика от 1 до 6.
# Если сытость < 20, то нужно поесть.
# Иначе, если еды в доме < 10, то сходить в магазин.
# Иначе, если денег в доме < 50, то работать.
# Иначе, если кубик равен 1, то работать.
# Иначе, если кубик равен 2, то поесть.
# Иначе играть.
# По такой логике эксперимента человеку надо прожить 365 дней.
#
# Реализуйте такую программу и создайте двух людей, живущих в одном доме. Проверьте работу программы несколько раз.
#
# Советы и рекомендации
# В большинстве случаев классы нужны не для того, чтобы с ними работать напрямую, а чтобы с их помощью создавать объекты
# , которые будут содержать необходимую информацию и смогут вызывать нужные методы. Наш случай не исключение: вам не
# нужно работать напрямую с классами, работайте с объектами, которые создаются при помощи этих классов. Глобальные
# переменные создают зависимости. Чем больше класс обращается к переменным, созданным снаружи класса, тем больше в
# классе появляется неопределённости (для работы с классом вам придётся отслеживать значения всех этих переменных).
# По возможности передавайте нужные данные в объект и записывайте их в атрибуты вместо обращения к глобальной переменной
# .

import random


# todo по заданию нужно чтобы люди жили в одном доме
class Human:
    day = 0

    def __init__(self, name, house):
        self.name = name
        self.hunger = 50
        self.house = house

    def eat(self):
        self.hunger += 10
        self.house.fridge -= 10

    def play(self):
        self.hunger -= 10

    def work(self):
        self.hunger -= 10
        self.house.money += 10

    def buy_food(self):
        self.house.fridge += 10
        self.house.money -= 10

    def live_a_day(self):
        cube = random.randint(1, 6)
        if self.hunger < 20:
            self.eat()
        elif self.house.fridge < 10:
            self.buy_food()
        elif self.house.money < 50:
            self.work()
        elif cube == 1:
            self.work()
        elif cube == 2:
            self.eat()
        else:
            self.play()


class House:
    START_FRIDGE = 50
    START_MONEY = 0

    def __init__(self):
        self.fridge = self.START_FRIDGE
        self.money = self.START_MONEY


my_house = House()
human_1 = Human('Жорик', my_house)
human_2 = Human('Толян', my_house)


while human_1.hunger >= 0 and human_2.hunger >= 0 and Human.day <= 365:
    Human.day += 1
    human_1.live_a_day()
    human_2.live_a_day()

if human_1.hunger < 0 or human_2.hunger < 0:
    print(f'Человек умер от голода на {Human.day} дн. Эксперимент закончен :(((')
elif Human.day > 365:
    print('Ура! Все выжили!')
