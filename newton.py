import math


def funct(k):
    return math.sin(k * 2)
    """ Edit this function"""


def d1(k, func, h=1e-6):
    """Derivative function"""
    return func(k + h) / h - func(k) / h


def d2(k, func, h=1e-6):
    """2nd Derivative function"""
    return d1(k + h, func) / h - d1(k, func) / h


def optimize(k, func, h=1e-6):
    """Newton Method"""
    if not callable(func):
        raise TypeError(f"Argument is not a function, it is of type {type(func)}")
    k1 = 1
    k0 = 0
    count = 0
    badStep = 0
    while abs(k1 - k0) > 0.001:
        """ Approximation algorithm"""
        k1 = k - d1(k, func, h) / d2(k, func, h)
        if k > k1:
            badStep += 1
        if badStep > 3:
            raise RuntimeError(
                f"At iteration {count}, optimization appears to be diverging"
            )
        k = k1
        count += 1
        if count > 1e9:
            """ Setting limit on while loop"""
            break
    return k, func(k)
