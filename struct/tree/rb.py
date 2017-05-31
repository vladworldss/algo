# coding: urf-8
from .base import _Node, _Tree


class Node(_Node):
    def __init__(self, key, *args, **kwargs):
        super().__init__(key, *args, **kwargs)
        self.red = False


class Tree(_Tree):
    def __init__(self, NodeCls=Node):
        super().__init__(NodeCls)

    def search(self, key, v=None):
        """
        Поиск ноды по ключу, начиная с v-вершины.
        Если не задана - ведем поиск начиная с корня.
        
        :param key: 
        :param v: 
        :return: 
        """
        if not v:
            v = self.root
        while v != self.nil and v.key != key:
            if key < v.key:
                v = v.left
            else:
                v = v.right
        return v

    def min(self, v=None):
        if not v:
            v = self.root
        while v != self.nil:
            v = v.left
        return v

    def max(self, v=None):
        if not v:
            v = self.root
        while v != self.nil:
            v = v.right
        return v

    def insert_key(self, key):
        self.insert_node(self.NodeCls(key))

    def insert_node(self, z):
        """
        Вставка осуществляется в 2 этапа:
            - проталкиваем ноду вниз, каждый раз выбирая нужное поддерево
            - производим перебалансировку
            
        :param node: 
        :return: 
        """
        x = self.root
        y = self.nil
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

