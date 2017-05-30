# coding: utf-8
"""
Модуль класса очереди с приоритетом (heap).
"""


class Heap(list):

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.quick_build_heap()
        #self.build_heap()

    @property
    def size(self):
        """
        Возвразает размер кучи

        :return: 
        """
        return len(self)

    def build_heap(self):
        """
        Стандартный метод построения кучи. 
        Сложность: O(Nlog(N)).
        """
        seq = self[:]
        self.clear()
        for item in seq:
            self.add_item(item)

    def quick_build_heap(self):
        """
        Быстрый способ построения кучи. Сначала строим дерево как есть, 
        потом "проталкиваем вниз" вершину.
        Сложность: O(N)
        """
        middle = int(self.size / 2)
        for i in range(middle, -1, -1):
            self.sift_down(i)

    def add_item(self, item):
        """
        Метод добавления элемента в кучу. 
        Сначала добавляет элемент в конец, потом проталкивает его наверх, если он больше родителя.
        Сложность: O(log(N))
        :param item: элемент кучи.
        """
        self.append(item)
        i = self.size - 1
        parent = int((i - 1) / 2)
        while (i > 0 and self[i] > self[parent]):
            tmp = self[i]
            self[i] = self[parent]
            self[parent] = tmp
            i = parent
            parent = int((i - 1) / 2)

    def sift_down(self, index):
        """
        Функция "проталкивания вниз" меньшего элемента.
        Сложность - O(log(N))

        :param index: 
        :return: 
        """
        while True:
            parent = index
            left_child = 2 * index + 1
            right_child = 2 * index + 2

            if left_child < self.size and self[parent] < self[left_child]:
                parent = left_child
            if right_child < self.size and self[parent] < self[right_child]:
                parent = right_child
            if parent == index:
                break
            tmp = self[index]
            self[index] = self[parent]
            self[parent] = tmp
            index = parent

    @property
    def pop_max(self):
        """
        Возвращает максимальный элемент кучи (root)
        :return: heap[0]
        """
        root = self[0]
        try:
            self[0] = self.pop()
        except IndexError:
            pass
        return root

    @staticmethod
    def heap_sort(L, reverse=True):
        """
        Метод "Сортировка кучей" или "Пирамидальная сортировка"
        Постоянная сложность: O(Nlog(N))
        
        :param L:
        :param reverse: будет ли список отсортирован в прямом (min->max) или обратном (max->min) порядке.
        :return: отсортированный список.
        """
        res = []
        h = Heap(L)
        for i in range(h.size - 1, -1, -1):
            res.append(h.pop_max)
            h.sift_down(0)
        if not reverse:
            res = [res[i] for i in range(len(res)-1, -1, -1)]
        return res
