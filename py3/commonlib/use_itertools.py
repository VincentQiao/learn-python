# -*- coding: utf-8 -*-
__author__ = 'Vincent'

import itertools
naturals = itertools.count(1)
i = 0
for n in naturals:
    i += 1
    if i > 4:
        break
    print(n)


cs = itertools.cycle('ABC')

for c in cs:
    i += 1
    if i > 10:
        break
    print(c)

ns = itertools.repeat('A', 3)
for n in ns:
    print(n)

new_naturals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, new_naturals)
print(list(ns))

for c in itertools.chain('ABC', 'XYZ'):
    print(c)

# groupby, 把迭代器中相邻的重复元素挑出来
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))