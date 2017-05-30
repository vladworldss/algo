# coding: utf-8

from itertools import chain


def sort(li):

    def _sort(L):
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
        left = list(filter(lambda x: x <= main, tail))
        right = list(filter(lambda x: x > main, tail))
        return chain(_sort(left), (main,), _sort(right))

    return list(_sort(li))
