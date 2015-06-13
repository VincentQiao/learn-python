# -*- coding: utf-8 -*-
__author__ = 'Vincent'
def calc_sums(*args):
    ax = 0
    for n in args:
        ax += n
    return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum

f = lazy_sum(1,2,3,4,5)
print(f)
print(f())

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


