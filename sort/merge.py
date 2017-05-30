# coding: utf-8


def sort(L):
    """
    Функция сортировки слиянием. 
    Рекурсивный метод.
    Сложность - Лучшее = O(Nlog(N));
                Среднее = O(Nlog(N));
                Худшее = O(Nlog(N));
    "Минусы":   на почти отсортированных массивах работает также, как и на хаотичных;
                требует дополнительной памяти размера N
    
    :param L: unsorted_list
    :return: sorted_list
    """

    def merge(a, b):
        """
        Функция слияния двух списков.
        Сложность - O(N)
        "Минусы" - требует вспомогательные данные (временный список храниния промежут рещзультата) 
        в худшем случае O(N)
        
        :param a: list 
        :param b: list
        :return: merge_list
        """
        c = []
        i = j = 0
        size = len(a), len(b)
        size_left, size_right = min(size), max(size)
        n = sum(size)
        for _ in range(n):
            try:
                left, right = a[i], b[j]
                if left < right:
                    c.append(left)
                    i += 1
                else:
                    c.append(right)
                    j += 1
            except IndexError:
                break
        if i < size_left:
            c.extend(a[i:])
        else:
            c.extend(b[j:])
        return c

    size = len(L)
    if size < 2:
        return L
    middle = int(size/2)
    left = sort(L[:middle])
    right = sort(L[middle:])
    return merge(left, right)
