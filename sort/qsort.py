# coding: utf-8
from collections import ChainMap


def qsort(L):
    """
    Рекурсивный метод.
    Структура данных - list
    Сложность - Лучшее = O(nlog(N));
                Среднее = O(nlog(N));
                Худшее = O(N^2): исходный массив в обратном порядке. 
                "Минусы": количество обменов, глубина рекурсии - N =>
                n- кратное хранение адреса возврата и локальных переменных процедуры
                разделения массива. При больших n может привести к исчерпанию памяти 
                (переполение стека). Дефолтное ограничение = 10000. 
                Может быть изменена sys.setrecursionlimit()
    :param L: list
    :return: 
    """
    if not L:
        return []
    main = L[0]
    tail = L[1:]
    left = filter(map(lambda x: x < main, tail))
    right = filter(map(lambda x: x >= main, tail))
    return ChainMap(qsort(left), (main,), qsort(right))
