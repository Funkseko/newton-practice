import math
def func(k):
    return math.sin(k*2)

def d1(k):
    return func(k+0.001)/0.001 - func(k)/0.001

def d2(k):
    return d1(k+0.001)/0.001 - d1(k)/0.001

def optimize(k):
    k1 = 0
    k0 = 0
    while not abs(k1-k0) > 0.00001:
        k0=k
        k1 = k -d1(k)/d2(2)
        k = k1
    return [k, func(k)]
