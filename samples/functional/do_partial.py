# -*- coding: utf-8 -*-
__author__ = 'vincent'

import functools


# def int2(x, base=2):
#     return int(x, base)

# 固定**kw
int2 = functools.partial(int, base=2)

# 固定 *args
max2 = functools.partial(max, 10)