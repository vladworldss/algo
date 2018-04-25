"""
Поиск значений в последовательностях
"""


def second_max(num_list):
    if len(num_list) < 2:
        raise IndexError
    pair = (num_list.pop(), num_list.pop())
    max1, max2 = max(pair), min(pair)
    while num_list:
        val = num_list.pop()
        if val > max1:
            max2 = max1
            max1 = val
        elif val > max2:
            max2 = val
