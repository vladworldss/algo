# coding: utf-8
"""
Модуль декораторов.
"""
from functools import wraps


def single_delegate(delegat, method):
    """
    Декоратор класса, осуществляющий делегирование.

    :param delegator: имя делегата.
    :param method: вызываемый метод.
    """
    def wrap(Class):
        @wraps(Class)
        def foo(self, *args, **kw):
            d = getattr(self, delegat)
            m = getattr(d, method)
            if not callable(m):
                raise TypeError(f"{type(m)} object is not callable")
            return m(*args, **kw)
        setattr(Class, method, foo)
        return Class
    return wrap


def multy_delegate(delegat, m, *meths):
    """
    Декоратор класса, осуществляющий делегирование.

    :param delegator: имя делегата.
    :param method: вызываемый метод.
    """
    def wrap(Class):
        @wraps(Class)
        def set_delegate_methods(_method):
            def foo(self, *args, **kw):
                d = getattr(self, delegat)
                m = getattr(d, _method)
                if not callable(m):
                    raise TypeError(f"{type(m)} object is not callable")
                return m(*args, **kw)
            return foo

        for method in (m, *meths):
            setattr(Class, method, set_delegate_methods(method))
        return Class
    return wrap
