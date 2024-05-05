# Задача 2. Поиск элемента — 2
# Что нужно сделать
# Пользователь вводит искомый ключ. Если он хочет, то может ввести максимальную глубину — уровень, до которого будет
# просматриваться структура.
# Напишите функцию, которая находит заданный пользователем ключ в словаре и выдаёт значение этого ключа на экран.
# По умолчанию уровень не задан. В качестве примера можно использовать такой словарь:

# Пример 1
# Введите искомый ключ: head
# Хотите ввести максимальную глубину? Y/N: n
# Значение ключа: {'title': 'Мой сайт'}
#
# Пример 2
# Введите искомый ключ: head
# Хотите ввести максимальную глубину? Y/N: y
# Введите максимальную глубину: 1
# Значение ключа: None
#
# Что оценивается:
# Основной функционал описан в отдельной функции(-ях).


site = {
    "html": {
        "head": {"title": "Мой сайт"},
        "body": {
            "h2": "Здесь будет мой заголовок",
            "div": "Тут, наверное, какой-то блок",
            "p": "А вот здесь новый абзац",
        },
    }
}


def search_key_with_depth(key, data, depth):
    result = None
    if depth > 0:
        if key in data:
            return data[key]
        for sub_struct in data.values():
            if isinstance(sub_struct, dict):
                result = search_key_with_depth(key, sub_struct, depth - 1)
                if result:
                    return result
            else:
                return result
    else:
        return result


def search_key(key, data):
    result = None
    if key in data:
        return data[key]
    for sub_struct in data.values():
        if isinstance(sub_struct, dict):
            result = search_key(key, sub_struct)
            if result:
                return result
        else:
            return result


select_key = input('Введите искомый ключ: ')
optional_depth = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if optional_depth == 'n':
    print(f'Значение ключа: {search_key(select_key, site)}')
elif optional_depth == 'y':
    max_depth = int(input('Введите максимальную глубину: '))
    print(f'Значение ключа: {search_key_with_depth(select_key, site, max_depth)}')

