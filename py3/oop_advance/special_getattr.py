# -*- coding: utf-8 -*-
__author__ = 'vincent'

class Student(object):

    def __init__(self):
        self.name = 'Vincent'

    def __getattr__(self, item):
        if item == 'score':
            return 99


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        if path != 'users':
            return Chain('%s/%s' % (self._path, path))
        else:
            return lambda name: Chain('%s/%s' % (self._path, name))

    def __str__(self):
        return self._path

    __repr__ = __str__

