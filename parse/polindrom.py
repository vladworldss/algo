# coding: utf-8
"""Функция определения, является ли передаваемая строка полиндромом."""


def skip_nonsymbls(_string):
    for ch in _string:
        if ch.isalnum():
            yield ch


def test(_symbols):
    _symbols = [ch for ch in skip_nonsymbls(_symbols)]
    size = len(_symbols)-1
    result = True
    for i, j in enumerate(range(size, -1, -1)):
        left, right = _symbols[i], _symbols[j]
        if not left == right:
            result = False
            break
    return result


if __name__ == '__main__':
    st = 'ab!ba#'
    print(f"{st} is polindrome = {test(st)}")
