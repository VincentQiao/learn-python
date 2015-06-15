# -*- coding: utf-8 -*-
__author__ = 'vincent'

# property, 负责把一个方法变成属性调用

class Student(object):
    # score is a property object, property 是一个内置的装饰器
    # 加@property, 把一个get_score方法变成属性
    # 只定义getter方法，不定义setter方法就是一个只读属性：
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width

# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution