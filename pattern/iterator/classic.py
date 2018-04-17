# coding: utf-8
"""
Классическая имплементация паттерна "Итератор".
Назначение: 
+ для доступа к содержимому агрегированных объектов без раскрытия их внутреннего представления;
+ для поддержки нескольких активных обходов одного и того же агрегированного объекта (желательно, но не обязательно);
+ для предоставления единообразного интерфейса с целью обхода различных агрегированных структур.

original: https://habrahabr.ru/post/337314/
"""
from abc import ABC, abstractmethod


class Aggregate(ABC):
    """
    Интерфейс класса составного объекта, 
    по которому может перемещаться итератор
    """
    @abstractmethod
    def iterator(self):
        """
        Вовзращает итератор.
        """
        pass


class Iterator(ABC):
    """
    Интерфейс класса итератора.
    """

    def __init__(self, collection, cursor):
        """

        :param collection: коллекция элементов (агрегатор), по которым перемещается итератор
        :param cursor: курсор перемещения
        """
        self._collection = collection
        self._cursor = cursor

    @abstractmethod
    def first(self):
        """
        Возвращает итератор к началу агрегата.
        """
        pass

    @abstractmethod
    def next(self):
        """
        Переходит на следующий элемент агрегата.
        Если достигнут конец последовательности - возбуждается StopIteration
        """
        pass

    @abstractmethod
    def current(self):
        """
        Возвращает текущий элемент
        """
        pass


class ListIterator(Iterator):
    """
    Реализация итератора для списка.
    """

    def __init__(self, collection, cursor):
        """
        Конструктор класса.

        :param collection: список
        :param cursor: индекс, с которого начнется перебор коллекции.
        Так же должна быть проверка -1 >= cursor < len(collection)
        """
        super().__init__(collection, cursor)

    def first(self):
        """
        Начальное положение курсора -1.
        В нашей реализации вначале необходимо вызвать next, который сдвинет курсор на 1.
        """
        self._cursor = -1

    def next(self):
        """
        Если курсор указывает на последний элемент, то вызываем StopIteration,
        иначе сдвигаем курсор на 1.
        """
        if (self._cursor + 1) >= len(self._collection):
            raise StopIteration
        self._cursor += 1

    def current(self):
        """
        Возвращаем текущий элемент.
        :return: elem of collections
        """
        return self._collection[self._cursor]


class ListCollection(Aggregate):
    """
    Реализация спискового агрегата.
    """

    __IteratorCls = ListIterator

    def __init__(self, collection):
        self._collection = list(collection)

    def iterator(self):
        return self.__IteratorCls(self._collection, -1)


def test():
    def ride_on_iter(iterator):
        """
        Генератор обхода итератора.
        В бесконечном цикле вызываем next(), пока не будет
        вызвано StopIteration.
        """
        while True:
            try:
                iterator.next()
                yield iterator.current()
            except StopIteration:
                break

    collection = (1, 2, 5, 6, 8)
    aggregate = ListCollection(collection)
    itr = aggregate.iterator()
    assert collection == tuple(ride_on_iter(itr))
