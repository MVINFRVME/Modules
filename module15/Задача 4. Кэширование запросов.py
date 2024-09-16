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

class LRUCache:
    """ Класс LRU Cache (Least Recently Used Cache). Хранит ограниченное количество
    запросов, а также автоматически удаляет самые старые при достижении лимита.
    """

    def __init__(self, capacity) -> None:
        self.elem_count = 0
        self.__capacity = capacity
        self.__cache = []

    @property
    def cache(self):
        """Геттер, который возвращает самый старый элемент."""
        return self.__cache[0]

    @cache.setter
    def cache(self, new_elem: tuple):
        """Добавляет кортеж (ключ : значение) в кэш. А в случае достижения лимита,
        удаляет первый элемент, а затем добавляет кортеж в конец. """
        if self.elem_count == self.__capacity:
            self.__cache.remove(self.__cache[0])
            self.elem_count -= 1
        self.__cache.append(new_elem)
        self.elem_count += 1

    def print_cache(self):
        """Метод выводит на экран текущий кэш."""
        print("LRU Cache:")
        for i in range(self.elem_count):
            print(f'{self.__cache[i][0]} : {self.__cache[i][1]}')

    def get(self, key):
        """Метод возвращает искомое значение по ключу."""
        for i in range(self.elem_count):
            if self.__cache[i][0] == key:
                return self.__cache[i][1]


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
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4
