# coding: utf-8


if __name__ == '__main__':
    from random import randint
    from struct.queue.heap import Heap

    l = [randint(1, 20) for _ in range(10)]
    heap_s = Heap.heap_sort(l, False)
    q_s = sorted(l)
    if heap_s == q_s:
        print('ok')
    else:
        print('error')