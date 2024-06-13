# Задача 4. Магия
# Что нужно сделать
# Для одной игры необходимо реализовать механику магии, где при соединении двух элементов получается новый. У нас есть
# четыре базовых элемента:
# «Вода», «Воздух», «Огонь», «Земля». Из них получаются новые: «Шторм», «Пар», «Грязь», «Молния», «Пыль», «Лава».

# Таблица преобразований:

# Вода + Воздух = Шторм;
# Вода + Огонь = Пар;
# Вода + Земля = Грязь;
# Воздух + Огонь = Молния;
# Воздух + Земля = Пыль;
# Огонь + Земля = Лава.

# Напишите программу, которая реализует все эти элементы. Каждый элемент необходимо организовать как отдельный класс.
# Если результат не определён, то возвращается None.

# Примечание: сложение объектов можно реализовывать через магический метод __add__, вот пример использования:

# class ExampleOne:
#     def __add__(self, other):
#         return ExampleTwo()

# class ExampleTwo:
#     answer = 'сложили два класса и вывели'

# first_example = ExampleOne()
# second_example = ExampleTwo()
# result = first_example + second_example
# print(result.answer)

# Дополнительно: придумайте свой элемент (или элементы) и реализуйте его взаимодействие с остальными.

class Water:
    name = 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None


class Air:
    name = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Water):
            return Storm()
        else:
            return None


class Fire:
    name = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        else:
            return None


class Earth:
    name = 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return None


class Storm:
    name = 'Шторм'


class Steam:
    name = 'Пар'


class Dirt:
    name = 'Грязь'


class Lightning:
    name = 'Молния'


class Dust:
    name = 'Пыль'


class Lava:
    name = 'Лава'


water = Water()
air = Air()
fire = Fire()
earth = Earth()
elements = [water, air, fire, earth]

for i_elem in elements:
    try:
        for j_elem in elements:
            print(f'{i_elem.name} + {j_elem.name} = {(i_elem + j_elem).name}')

    except AttributeError:
        continue
