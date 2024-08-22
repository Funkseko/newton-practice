import math


def funct(k):
    return math.sin(k * 2)  # Edit this function


def d1(k, func):
    return func(k + 0.001) / 0.001 - func(k) / 0.001


def d2(k, func):
    return d1(k + 0.001, func) / 0.001 - d1(k, func) / 0.001


def optimize(k, func):
    k1 = 1
    k0 = 0
    while abs(k1 - k0) > 0.00001:
        k0 = k
        k1 = k - d1(k, func) / d2(k, func)
        k = k1
    return [k, func(k)]
