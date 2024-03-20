# Задание 7. Анализ слова — 2
# Что нужно сделать
# Продолжите писать анализаторы для текста. Теперь необходимо реализовать код, с помощью которого
# можно определять палиндромы, то есть слова, которые читаются одинаково слева направо и справа налево.
#
# Напишите такую программу.
#
# Пример 1:
#
# Введите слово: мадам
#
# Слово является палиндромом
#
# Пример 2:
#
# Введите слово: abccba
#
# Слово является палиндромом
#
# Пример 3:
#
# Введите слово: abbd
#
# Слово не является палиндромом
#

word = list(input('Введите слово: '))
new_word = []
index = 1

for _ in word:
    symbol = word[-index]
    new_word.append(symbol)
    index += 1

if word == new_word:
    print('Слово является палиндромом.')
else:
    print('Слово не является палиндромом.')