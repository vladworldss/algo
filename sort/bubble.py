# coding: utf-8


def sort(L):
    """
    Пузырьковая сортировка.
    Сложность - Лучший = O(N);
                Средний = O(N^2);
                Худший = O(N^2).

    :param L: unsorted_list
    :return: sorted_list
    """
    if not isinstance(L, list):
        raise TypeError('Argument must be a list.')
    size = len(L)
    n = 1
    while n < size:
        for i in range(size-n):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
        n += 1
    return L
