# -*- coding: utf-8 -*-
__author__ = 'vincent'

def fn(self, name='world'):
    print('Hello, %s.' % name)

Hello = type('Hello', (object, ), dict(hello=fn))
h = Hello()
h.hello()
print(type(Hello))
print(h)
