# -*- coding: utf-8 -*-
__author__ = 'vincent'

# 虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器。

import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)