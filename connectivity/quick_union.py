# coding: utf-8
"""
Задача связности методом быстрого объединения

"""
from template import Connectivity, main


class QuickUnion(Connectivity):
    """
    Класс быстрого объединения
    Сложность = (худший) O(M*N/2) -> O(M*N)
    """
    def union(self, p, q):
        root_p, root_q = self.root(self.arr[p]), self.root(self.arr[q])
        if root_p != root_q:
            self.arr[root_p] = root_q
            print(p, q)

    def root(self, i):
        parent = self.arr[i]
        if parent == i:
            return i
        else:
            return self.root(parent)


class WeightedQuickUnion(QuickUnion):
    """
    Класс взвешенного быстрого объединения
    Сложность = O(M*log(N))
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sz = [1 for _ in range(self.size)]

    def union(self, p, q):
        root_p, root_q = self.root(self.arr[p]), self.root(self.arr[q])
        if root_p != root_q:
            if self.sz[root_p] < self.sz[root_q]:
                self.arr[root_p] = root_q
                self.sz[root_q] += self.sz[root_p]
            else:
                self.arr[root_q] = root_p
                self.sz[root_p] += self.sz[root_q]
            print(p, q)


if __name__ == '__main__':
    main(WeightedQuickUnion)
