def _sum(a, b):
    if not b:
        return a
    xor = a ^ b
    _and = (a & b) << 1
    return _sum(xor, _and)


def test(a, b):
    s_1 = sum((a, b))
    s_2 = _sum(a, b)
    if s_1 != s_2:
        raise Exception('Wrong!')
    print('\nEquile')

test(100, 1)
