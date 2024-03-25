# Задание 6. Бегущие цифры
#
# Что нужно сделать
# Вы пишете программу для маленького табло, в котором циклически повторяется
# один и тот же текст или числа, например как в метро, автобусах или трамваях.
# Дан список из N элементов и целое число K. Напишите программу, которая циклически
# сдвигает элементы списка вправо на K позиций.
# Используйте минимально возможное количество операций присваивания.
#
# Пример 1:
#
# Сдвиг: 1
#
# Изначальный список: [1, 2, 3, 4, 5]
#
# Сдвинутый список: [5, 1, 2, 3, 4]
#
# Пример 2:
#
# Сдвиг: 3
#
# Изначальный список: [1, 4, –3, 0, 10]
#
# Сдвинутый список: [–3, 0, 10, 1, 4]

original_list = [1, 2, 3, 4, 5]
new_list = []
shift = int(input('Сдвиг: '))

for i in range(shift):
    new_list.append(original_list[-shift + i])

remained_iterations = len(original_list) - shift

for i, value in enumerate(original_list):
    if i >= remained_iterations:
        break
    else:
        new_list.append(value)

print(f'Сдвинутый список: {new_list}')

# ok
