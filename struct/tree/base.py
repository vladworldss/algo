# coding: urf-8


class _Node(object):
    """
    Базовый класс узла.
    """
    def __init__(self, key, *args, **kw):
        self.key = key
        self.left = self.right = self.p = None


class _Tree(object):
    """
    Базовый класс узла.
    """
    def __init__(self, NodeCls=_Node, *args, **kw):
        self.NodeCls = NodeCls
        self.nil = self.NodeCls(key=None)
        self.root = self.nil
