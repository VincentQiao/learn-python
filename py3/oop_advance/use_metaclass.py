# -*- coding: utf-8 -*-
__author__ = 'vincent'

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class Mylist(list, metaclass=ListMetaclass):
    pass

L = Mylist()
L.add(1)
print(L)