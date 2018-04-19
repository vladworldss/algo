# coding: utf-8

"""Reverse linked list."""


class Node:
    """Linked list is either None or a value and a link to the next list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def reverse_list(head, tail=None):
    while head:
        head.next, tail, head = tail, head, head.next
    return tail


def print_list(head, end='\n'):
    while head:
        print(head.data, end=' -> ' if head.next else '')
        head = head.next
    print(end=end)


def test():
    head = Node(1, Node(2, Node(3, Node(4))))
    print_list(head)
    print_list(reverse_list(head))


if __name__ == "__main__":
    test()
