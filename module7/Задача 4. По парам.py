# Что нужно сделать
# Напишите программу, которая инициализирует список из 10 случайных целых чисел, а затем делит эти числа на пары
# кортежей внутри списка. Выведите результат на экран.
# Дополнительно: решите задачу несколькими способами.

# Пример:
# Оригинальный список: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Новый список: [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]

# Что оценивается:
# Для решения используются list comprehensions.

import random


rand_list = [random.randint(0, 10) for _ in range(10)]
tuple_pairs_list = [(rand_list[i - 1], rand_list[i]) for i in range(1, len(rand_list) + 1, 2)]
print(f'Оригинальный список: {rand_list}\n'
      f'Новый список: {tuple_pairs_list}')


# или
rand_list = list()

for dig in range(10):
    rand_list.append(random.randint(1, 10))

tuple_pairs_list = list()
for i_dig in range(0, len(rand_list), 2):
    if i_dig + 1 < len(rand_list):
        tuple_pairs_list.append((rand_list[i_dig], rand_list[i_dig + 1]))

print(f'\nОригинальный список: {rand_list}'
      f'\nНовый список: {tuple_pairs_list}')
