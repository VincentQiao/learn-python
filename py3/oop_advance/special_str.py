# -*- coding: utf-8 -*-
__author__ = 'vincent'

class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__

# test
s = Student('Bob')
print(s)
s

