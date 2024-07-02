# Задача 6. Абстрактный класс
# Контекст
# Вы работаете в компании, занимающейся разработкой программного обеспечения для архитектурных проектов. Вам необходимо
# разработать программу для расчёта площади различных геометрических фигур, таких как круги, прямоугольники и
# треугольники.

# Задача
# Создайте:
# класс Shape, который будет базовым классом для всех фигур и будет хранить пустой метод area, который наследники должны
# переопределить;
# класс Circle;
# класс Rectangle;
# класс Triangle.
# Классы Circle, Rectangle и Triangle наследуют от класса Shape и реализуют метод для вычисления площади фигуры.

# Дополнительно: изучите информацию о работе с абстрактными классами.

# На основе этой информации сделайте так, чтобы:

# Нельзя было создавать объекты класса Shape.
# Наследники класса Shape переопределяли его метод area, чтобы объекты этих классов можно было использовать.

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


cir = Circle(5)
rec = Rectangle(2, 3)
tri = Triangle(3, 4)
print(f'Площадь круга: {cir.area()}\n'
      f'Прямоугольника: {rec.area()}\n'
      f'Треугольника: {tri.area()}')

sh = Shape() # должно вызывать ошибку

# todo ok, первую задачу можно было тоже через ABC сделать
