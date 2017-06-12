# coding: utf-8
"""
Задача связности методом быстрого поиска.
Сложность: O(N*M)
N- число объектов;
M- число операций объединений.
"""
from template import Connectivity


class QuickFind(Connectivity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def union(self, p, q):
        i, j = self.arr[p], self.arr[q]
        if i != j:
            for k, val in enumerate(self.arr):
                if val == i:
                    self.arr[k] = j
            print(p, q)


if __name__ == '__main__':
    c = QuickFind()
    c.main()
