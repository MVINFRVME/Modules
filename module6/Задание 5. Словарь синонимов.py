# Задание 5. Словарь синонимов
# Что нужно сделать
# Одна библиотека поручила вам написать программу для оцифровки словарей синонимов.
# На вход в программу подаётся N пар слов. Каждое слово является синонимом для своего парного слова.
# Реализуйте код, который составляет словарь синонимов (все слова в словаре различны), затем запрашивает у пользователя
# слово и выводит на экран его синоним. Обеспечьте контроль ввода: если такого слова нет, выведите ошибку и запросите
# слово ещё раз. При этом проверка не должна зависеть от регистра символов.
#
# Пример
# Введите количество пар слов: 3
# Первая пара: Привет — Здравствуйте
# Вторая пара: Печально — Грустно
# Третья пара: Весело — Радостно
# Введите слово: интересно
# Такого слова в словаре нет.
# Введите слово: здравствуйте
# Синоним: Привет

pairs_num = int(input('Введите количество пар слов: '))
byword_dict = dict()

for pair in range(1, pairs_num + 1):
    bywords = input(f'{pair} пара: ').lower().split(' - ')
    byword_dict[bywords[0]] = bywords[1]

is_in_dict = False

while True:
    if is_in_dict:
        break

    check_word = input('Введите слово: ').lower()
    for key, value in byword_dict.items():
        if key == check_word:
            print(f'Синоним: {value}')
            is_in_dict = True
            break
        elif value == check_word:
            print(f'Синоним: {key}')
            is_in_dict = True
            break
    else:
        print('Такого слова в словаре нет.')

# я бы добавлял для каждой пары две записи в словарь, т.е. для Привет - Здраствуйте словарь был бы
# {"привет": "Здраствуйте", "Здраствуйте": "привет"}
