# coding: utf-8
from struct.queue.heap import Heap


def sort(L, *args):
    sort.__doc__ = Heap.sort.__doc__
    return Heap.sort(L, *args)
