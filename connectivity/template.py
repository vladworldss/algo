# coding: utf-8
import sys


class Connectivity(object):

    def __init__(self, size=None):
        self.size = size
        self.arr = [i for i in range(self.size)]

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        if not val:
            self.__size = int(input('Get array size: \n'))
        else:
            self.__size = val

    def find(self):
        raise NotImplementedError

    def union(self, *args):
        raise NotImplementedError

    def main(self):
        while True:
            try:
                pair = [int(x) for x in input('Get int pair (p, q): \n').split()]
                self.union(*pair)
            except KeyboardInterrupt:
                print([i for i in range(self.size)])
                print(self.arr)
                sys.exit()
            except TypeError:
                continue


def main(Cls, *args, **kw):
    inst = Cls(*args, **kw)
    inst.main()
