# Задача 4. Кэширование запросов
# Контекст
# Вы разрабатываете программу для кэширования запросов к внешнему API. Часто повторяющиеся запросы занимают много
# времени, поэтому вы решаете создать класс LRU Cache (Least Recently Used Cache), который будет хранить ограниченное
# количество запросов и автоматически удалять самые старые при достижении лимита. Это позволит значительно ускорить
# повторяющиеся запросы, так как данные будут браться из кэша, а не отправляться повторно.
#
# Задача
# Создайте класс LRU Cache, который хранит ограниченное количество объектов и, при превышении лимита, удаляет самые
# давние (самые старые) использованные элементы.
# Реализуйте методы добавления и извлечения элементов с использованием декораторов property и setter.
# @property
# def cache(self): # этот метод должен возвращать самый старый элемент
# ...
# @cache.setter
# def cache(self, new_elem): # этот метод должен добавлять новый элемент
# ...
# Советы
# Не забывайте обновлять порядок использованных элементов. В итоге должны удаляться давно использованные элементы,
# а не давно добавленные, так как давно добавленный элемент может быть популярен, и его удаление не поможет ускорить
# новые запросы.

# Пример:
#
# # Создаём экземпляр класса LRU Cache с capacity = 3
# cache = LRUCache(3)
# # Добавляем элементы в кэш
# cache.cache = ("key1", "value1")
# cache.cache = ("key2", "value2")
# cache.cache = ("key3", "value3")
# # # Выводим текущий кэш
# cache.print_cache() # key1 : value1, key2 : value2, key3 : value3
# # Получаем значение по ключу
# print(cache.get("key2")) # value2
# # Добавляем новый элемент, превышающий лимит capacity
# cache.cache = ("key4", "value4")
# # Выводим обновлённый кэш
# cache.print_cache() # key2 : value2, key3 : value3, key4 : value4
# Ожидаемый вывод в консоли:
#
# LRU Cache:
# key1 : value1
# key2 : value2
# key3 : value3
# value2git
# LRU Cache:
# key3 : value3
# key2 : value2
# key4 : value4

from typing import List


class LRUCache:
    """ Класс LRU Cache (Least Recently Used Cache). Хранит ограниченное количество
    запросов, а также автоматически удаляет самые старые при достижении лимита.

        Arguments:
           capacity (int): лимит элементов в кэше

        Attributes:
            __elem_count (int): Счетчик количества элементов в кэше на данный момент.
            __cache (List): сам кэш, представленный в виде списка элементов.

    """

    def __init__(self, capacity) -> None:
        self.__elem_count = 0
        self.__capacity = capacity
        self.__cache = []

    @property
    def cache(self) -> List:
        """Геттер, возвращающий список, в котором находится индекс(ы) самого старого(непопулярного) элемента(ов)."""
        old_elems = []  # Список для хранения индекса наименее популярного элемента(ов).
        min_requests = self.__cache[0][1] # Зададим первый элемент как минимальный, чтобы было с чем сравнивать.
        for elem in self.__cache: # Найдем самое минимальное кол-во запросов элемента.
            requests = elem[1]
            if requests <= min_requests:
                min_requests = requests

        for i in range(self.__elem_count): # Найдем индекс(ы) этого элемента.
            requests = self.__cache[i][1]
            if requests == min_requests:
                old_elems.append(i)

        return old_elems

    @cache.setter
    def cache(self, new_elem: tuple) -> None:
        """Добавляет список [(ключ : значение), популярность элемента] в кэш. А в случае достижения лимита,
        удаляет самый старый элемент, а затем добавляет список в конец. """
        if self.__elem_count == self.__capacity:
            i_elem_for_delete = self.cache
            for i in sorted(i_elem_for_delete, reverse=True): # Отсортируем список в порядке убывания,
                # чтобы не произошли ошибки, связанные с удалением.
                self.__cache.pop(i)
                self.__elem_count -= 1

        requests = 0 # При помощи переменной requests будем определять популярность элемента
        self.__cache.append([new_elem, requests])
        self.__elem_count += 1

    def print_cache(self) -> None:
        """Метод выводит на экран текущий кэш."""
        print("LRU Cache:")
        for elem in self.__cache:
            key, value = elem[0][0], elem[0][1]
            print(f'{key} : {value}')

    def get(self, curr_key) -> str:
        """Метод возвращает искомое значение по ключу, а также увеличивает его популярность на 1."""
        for elem in self.__cache:
            key, value = elem[0][0], elem[0][1]
            if curr_key == key:
                elem[1] += 1 # увеличиваем популярность на 1
                return value


# Создаём экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# # # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

# # Получаем значение по ключу
print(cache.get("key2"))  # value2

# # Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# # Выводим обновлённый кэш
cache.print_cache()  # key2 : value2, key4 : value4
