# coding: utf-8
"""
Имплементация паттерна "Итератор" в стиле Python.
original: https://habrahabr.ru/post/337314/
"""

from collections.abc import Iterator, Iterable


class ListIterator(Iterator):

    def __init__(self, collection, cursor):
        self._collection = collection
        self._cursor = cursor

    def __next__(self):
        if (self._cursor + 1) >= len(self._collection):
            raise StopIteration
        self._cursor += 1
        return self._collection[self._cursor]


class ListCollection(Iterable):

    _IteratorCls = ListIterator

    def __init__(self, collection):
        self._collection = collection

    def __iter__(self):
        return self._IteratorCls(self._collection, -1)


def test():
    def ride_on_iter(iterator):
        """
        Генератор обхода итератора.
        В бесконечном цикле вызываем next(), пока не будет
        вызвано StopIteration.
        """
        while True:
            try:
                yield next(iterator)
            except StopIteration:
                break

    def friendly_ride(iterator):
        while True:
            item = next(iterator, None)
            if item is None:
                break
            yield item

    collection = (1, 2, 5, 6, 8)
    aggregate = ListCollection(collection)
    assert collection == tuple(aggregate)

    itr = iter(aggregate)
    assert collection == tuple(ride_on_iter(itr))

    itr = iter(aggregate)
    assert collection == tuple(friendly_ride(itr))
