import math


def funct(k):
    return math.sin(k * 2)  
    """ Edit this function"""


def d1(k, func, h = 1e-6): 
    """Derivative function"""
    return func(k + h) / h - func(k) / h


def d2(k, func, h = 1e-6): 
    """ 2nd Derivative function"""
    return d1(k + h, func) / h - d1(k, func) / h


def optimize(k, func, h = 1e-6): 
    """ Newton Method"""
    k1 = 1
    k0 = 0
    count = 0
    while abs(k1 - k0) > 0.001:
        """ Approximation algorithm"""
        k0 = k
        k1 = k - d1(k, func) / d2(k, func)
        k = k1
        count += 1
        if count > 1e9: 
            """ Setting limit on while loop"""
            break
    return [k, func(k)]

import numdifftools as nd
import numpy as np
def mult_optimize(X,func, h = 1e-4):
    while pow(np.sum((X1-X)**2),0.5) > h:
        X1 = X - np.linalg.inv(nd.hessian(func))*gradient(func)
        X=X1
    return [X,func(X)]
beta0 = 1.5
beta2 = 0.6

y = beta0 + beta1*x+np.random.normal(size=n)

def funct(theta):
    return np.sum((y- theta[0] - theta[1]*x)**2)
