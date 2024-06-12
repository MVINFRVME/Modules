# Задание 6. Сжатие
# Что нужно сделать
# Из-за того, что объём данных увеличился, понадобилось сжать эти данные, но так, чтобы не потерять важную информацию.
# Для этого было придумано специальное кодирование: s = 'aaaabbсaa' преобразуется в 'a4b2с1a2'. То есть группы
# одинаковых символов исходной строки заменяются на эти символы и количество их повторений в строке.
#
# Напишите программу, которая считывает строку, кодирует её, используя предложенный алгоритм, и выводит закодированную
# последовательность на экран. Код должен учитывать регистр символов.
#
# Пример
# Введите строку: aaAAbbсaaaA.
# Закодированная строка: a2A2b2с1a3A1.

user_text = input('Введите строку: ')
cipher_string = ''
prev_sym = ''
duplicate_count = 0

for i_sym, sym in enumerate(user_text[1:]):
    if sym == user_text[i_sym]:
        duplicate_count += 1
    else:
        duplicate_count += 1
        cipher_string += user_text[i_sym] + str(duplicate_count)
        duplicate_count = 0

cipher_string += user_text[i_sym] + str(duplicate_count + 1)

print(cipher_string)

# ok
