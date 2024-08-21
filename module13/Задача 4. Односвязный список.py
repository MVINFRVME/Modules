# Задача 4. Односвязный список
# Что нужно сделать
# Мы продолжаем тему структур данных и алгоритмов. И в этот раз вам нужно реализовать односвязный список.
# Связный список — это структура данных, которая состоит из элементов, называющихся узлами. В узлах хранятся данные, а
# между собой узлы соединены связями. Связь — это ссылка на следующий или предыдущий элемент списка.
# В односвязном списке связь — это ссылка только на следующий элемент, то есть в нём можно передвигаться только в
# сторону конца списка. Узнать адрес предыдущего элемента, опираясь на содержимое текущего узла, невозможно.
# Реализуйте такую структуру данных без использования стандартных структур Python (list, dict, tuple и прочие) и
# дополнительных модулей.
# Для реализации напишите два класса: Node и LinkedList. В Node должна быть логика работы одного узла (хранение данных
# и указателя).
# Для структуры реализуйте следующие методы:
# append — добавление элемента в конец списка;
# get — получение элемента по индексу;
# remove — удаление элемента по индексу.
# Дополнительно: сделайте так, чтобы по списку можно было итерироваться с помощью цикла.
#
# Пример основной программы:

# my_list = LinkedList()
# my_list.append(10)
# my_list.append(20)
# my_list.append(30)
# print('Текущий список:', my_list)
# print('Получение третьего элемента:', my_list.get(2))
# print('Удаление второго элемента.')
# my_list.remove(1)
# print('Новый список:', my_list)

# Результат:
# Текущий список: [10 20 30]
# Получение третьего элемента: 30
# Удаление второго элемента.
# Новый список: [10 30]
#
# Что оценивается
# Результат вычислений корректен.
# Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
# При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
# Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры.
# Для создания нового класса на основе уже существующего используется наследование.
# Формат вывода соответствует примеру.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Классы и методы/функции имеют прописанную документацию.
# Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs). Если функция/метод ничего не
# возвращает, то используется None.

from typing import Any, Optional


class Node:
    """Класс Node(узел)

    Args:
        value (Optional[Any]): данные, которые хранятся в узле
        next (Optional[Node]): ссылка на следующий узел

    """
    def __init__(self, value: Optional[Any] = None, next: Optional['Node'] = None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Метод __str__ возвращает строковое представление узла в формате: Node [value]"""
        return f'Node [{self.value}]'


class LinkedList:
    """ Класс LinkedList (Односвязный список)

    Attributes:
        head (Optional[Node]): головной элемент списка (указатель)
        length (int): длина односвязного списка (кол-во его элементов)
    """
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length = 0

    def __str__(self) -> str:
        """Метод __str__ возвращает строковое представление односвязного списка
         в формате: LinkedList [value value ... ]"""
        if self.head is not None:
            current = self.head
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return 'LinkedList [{values}]'.format(values=' '.join(values))
        return 'LinkedList []'

    def append(self, elem: Any) -> None:
        """Метод append добавляет новый узел в односвязный список.
        Если список пустой, то создает узел и объявляет его головным элементом.
        Если же узлы уже есть, то проходимся по всем узлам(начиная с головы) и связываем последний узел с новым.
        Также с добавлением элемента увеличивает длину списка на 1.
        """
        new_node = Node(elem)
        if self.head is None:
            self.head = Node(elem)
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.length += 1

    def remove(self, index: int) -> None:
        """Метод remove удаляет узел по его индексу.

        :param index: Передается индекс для удаления
        :type index: int

        :raises IndexError: если длина списка равна нулю или передаваемый индекс
        превышает длину списка
        """
        cur_node = self.head  # указатель текущего узла
        cur_index = 0  # текущий индекс
        if self.length == 0 or self.length <= index:
            raise IndexError

        if cur_node is not None:
            if index == 0: # можно объединить через and
                self.head = cur_node.next
                self.length -= 1
                return

        while cur_node is not None:
            if cur_index == index:
                break
            prev = cur_node
            cur_node = cur_node.next
            cur_index += 1

        prev.next = cur_node.next
        self.length -= 1

    def get(self, index: int) -> Node:
        """Метод get позволяет получить узел по его индексу.

        :param index: Передается индекс для получения узла
        :type index: int

        :return cur_node: возвращает указанный узел
        :rtype cur_node: Node

        :raises IndexError: если длина списка равна нулю или передаваемый индекс
        превышает длину списка
        """
        cur_node = self.head
        cur_index = 0

        if self.length == 0 or self.length < index:
            raise IndexError

        while cur_index < index:
            cur_node = cur_node.next
            cur_index += 1
        return cur_node


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print(my_list)
my_list.remove(1) # todo так падает с ошибкой
print(my_list)
print(my_list.get(1))
