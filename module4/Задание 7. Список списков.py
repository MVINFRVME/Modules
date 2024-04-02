# Задание 7. Список списков
# Что нужно сделать
# Дан многомерный список:
#
# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
#
# Напишите код, который раскрывает все вложенные списки, то есть оставляет лишь внешний список. Для решения используйте
# только list comprehensions.
#
# Ответ: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

opened_list = [dig for second_list in nice_list for first_list in second_list for dig in first_list]

print(opened_list)
