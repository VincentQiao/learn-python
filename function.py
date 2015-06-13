# -*- coding: utf-8 -*-
__author__ = 'Vincent'

from functools import reduce
from collections import Iterator, Iterable

def triangles():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0]+a, a+[0])]

n = 0
for t in triangles():
    print(t)
    n += 1
    if n == 10:
        break

def f(x):
    return x * x

def add(x, y):
    return x + y

def char2int(s):
    def fn(x, y):
        return 10 * x + y

    def char2num(c):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]
    return reduce(fn, map(char2num, s))

def normalize(name):
    def wrapper(a_name):
        return str.upper(a_name[0])+str.lower(a_name[1:])

    return map(wrapper, name)
# print (normalize(['liSa', 'vINcent', 'Vicky']))


from functools import reduce

def prod(int_list):
    def multiply(x, y):
        return x * y

    return reduce(multiply, int_list)
# print prod(range(1,11))

def str2float(s):
    if s.find('.') != -1:
        digit_place = len(s) - s.find('.') - 1
        s = s.split('.')[0] + s.split('.')[1]
    else:
        digit_place = 0
    return 10 ** (-digit_place) * char2int(s)
# print str2float('1234.56'), '6576.11231', '0.123', '1234'

# filter

def is_odd(n):
    return n % 2 == 1

# only for python 3.3
def primes():
    def _odd_iter():
        n = 3
        while True:
            yield n
            n += 2

    def _not_divisible(n):
        return lambda x: x % n > 0

    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)
# for n in primes():
#     if n < 100:
#         print(n)
#     else:
#         break
#

# print(filter(is_odd, range(1, 21)))

