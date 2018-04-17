# coding: utf-8
"""
Обзор итерируемых объектов.

original: https://habrahabr.ru/post/337314/
"""
import pytest
from collections.abc import Iterable
from random import randint
from string import ascii_letters


class SomeIterable1(Iterable):

    def __iter__(self):
        pass


def test_1():
    """
    Итерируемый объект это любой объект который реализует метод __iter__.
    """
    assert isinstance(SomeIterable1(), Iterable) is True


class SomeIterable2:

    def __iter__(self):
        pass


def test_2():
    """
    Итерируемый объект - это любой объект который реализует метод __iter__.
    Итерируемый объект — это любой объект, от которого встроенная функция iter()
    может получить итератор.
    Последовательности(abc.Sequence) всегда итерируемые, поскольку они реализуют метод __getitem__
    """
    assert isinstance(SomeIterable2(), Iterable) is True

    with pytest.raises(TypeError):
        itr = iter(SomeIterable2())


class SomeIterable3:

    """
    Функцию iter() использует например цикл for для получения итератора.
    Функция iter() в первую очередь для получения итератора из объекта,
    вызывает его метод __iter__.
    Если метод не реализован, то она проверяет наличие метода __getitem__ и если он реализован,
    то на его основе создается итератор. __getitem__ должен принимать индекс с нуля.
    Если не реализован ни один из этих методов, тогда будет вызвано исключение TypeError.
    """
    def __getitem__(self, key):
        return ascii_letters[key]


def test_3():
    """
    Создание итератора из объекта класса, имеющего __getitem__.
    """
    assert list([x for x in SomeIterable3()])

# -----------
# uses iter()
# -----------

ITER_DOC = """
iter() можно вызывать с двумя аргументами, что позволит создать из вызываемого объекта
(функция или класс с реализованным методом __call__) итератор. 
Первый аргумент должен быть вызываемым объектом, а второй — неким ограничителем. 
Вызываемый объект вызывается на каждой итерации и итерирование завершается, 
когда возбуждается исключение StopIteration или возвращается значения ограничителя.
"""


def test_call():
    """
    Использование функции в качестве итерируемого объекта.
    :return:
    """
    def dsix():
        return randint(1, 6)

    assert [x for x in iter(dsix, 6)]


class ProgrammingLanguages:

    """
    Вместо функции можно использовать классы с перегруженным
    методом __call__.
    """

    _name = ("Python", "Golang", "C#", "C", "C++", "Java", "SQL", "JS")

    def __init__(self, first=None):
        self._name_size = len(self._name)
        self.index = (-1 if first is None else
                      self._name.index(first) - 1)

    def __call__(self):
        self.index += 1
        if self.index < self._name_size:
            return self._name[self.index]
        raise StopIteration


def test_call_cls():

    # получение всех значений начиная с C#
    all_from_c_sharp = ["C#", "C", "C++", "Java", "SQL", "JS"]
    pl = ProgrammingLanguages("C#")
    assert [lang for lang in iter(pl, None)] == all_from_c_sharp

    # получение значений до C
    all_before_c_sharp = ["Python", "Golang", "C#"]
    pl = ProgrammingLanguages()
    assert [lang for lang in iter(pl, "C")] == all_before_c_sharp


# __Yield from
def test_yield_from():

    def foo(it):
        for x in it:
            yield from x

    items = [[1,2,3], [4,5,6]]
    assert list(range(1, 7)) == list(foo(items))


def flatten(items, ignore_types=(str, bytes)):
    """
    Генератор, преобразующий итерируемый объект любой вложенности в
    одномерный. Использует рекурсию.

    str, bytes - являются итерируемыми объектами, но их хотим возвращать целыми
    """
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


def test_flatten():
    items = [1, 2, [3, 4, [5, 6], 7], 8, ('A', ['B', 'C'])]
    assert list(flatten(items)) == [1, 2, 3, 4, 5, 6, 7, 8, 'A', 'B', 'C']

