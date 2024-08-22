import math


def funct(k):
    return math.sin(k * 2)  ''' Edit this function'''


def d1(k, func, h = 1e-6): '''Derivative function'''
    return func(k + h) / h - func(k) / h


def d2(k, func, h = 1e-6): ''' 2nd Derivative function'''
    return d1(k + h, func) / h - d1(k, func) / h


def optimize(k, func, h = 1e-6): ''' Newton Method'''
    k1 = 1
    k0 = 0
    count = 0
    while abs(k1 - k0) > 0.001:''' Approximation algorithm'''
        k0 = k
        k1 = k - d1(k, func) / d2(k, func)
        k = k1
        count += 1
        if count > 1e9: ''' Setting limit on while loop'''
            break
    return [k, func(k)]
