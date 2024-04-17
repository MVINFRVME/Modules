# Задание 1. Меню ресторана
# Что нужно сделать
# Ресторан заказал вам приложение, которое в один клик отображает пользователю меню. Для работы ресторан предоставил вам
# свой сайт, где можно найти меню в виде идущих подряд названий блюд.
# Напишите программу, которая выводит меню на экран. На вход подаётся строка из названий блюд, разделённых символом «;»,
# а на выходе названия перечисляются через запятую и пробел.
#
# Пример:
#
# Доступное меню: утиное филе;фланк-стейк;банановый пирог;плов.
#
# Сейчас в меню есть: утиное филе, фланк-стейк, банановый пирог, плов.

available_menu = 'утиное филе;фланк-стейк;банановый пирог;плов.'
print(f'Доступное меню: {available_menu}')

temporary_list = available_menu.split(';') # todo вот это строка не нужна, ты temporary_list больше не пользуешься

# now_in_menu = ', '.join(temporary_list)

now_in_menu = available_menu.replace(';', ', ')
print(f'Сейчас в меню {now_in_menu}')

# можно еще через replace сделать
# ok
