# coding: utf-8
"""
Функции бинарного поиска
"""


def empty_list(func):
    def foo(sorted_list, key):
        if not sorted_list:
            return False
        return func(sorted_list, key)
    return foo


@empty_list
def search(sorted_list, key):
    """
    Банарный поиск элемента в отсортированном массиве.
    """
    size = len(sorted_list)
    left = 0
    right = size - 1
    found = False

    while (left <= right) and (not found):
        middle = (left + right) // 2
        middle_value = sorted_list[middle]
        if middle_value == key:
            found = True
        elif key < middle_value:
            right = middle - 1
        else:
            left = middle + 1
    return found


@empty_list
def recurse_search(sorted_list, key):
    """
    Реккурсивная реализация бинарного поиска.
    """
    size = len(sorted_list)
    middle = size // 2
    middle_value = sorted_list[middle]
    if middle_value == key:
        return True

    if key <= middle_value:
        return recurse_search(sorted_list[:middle_value], key)
    else:
        return recurse_search(sorted_list[middle_value:], key)


def test():
    l = list(range(6))
    empty_l = []

    for fun in [search, recurse_search]:
        assert fun(l, 3) is True
        assert fun(l, 99) is False
        assert fun([1], 1) is True
        assert search(empty_l, 99) is False
