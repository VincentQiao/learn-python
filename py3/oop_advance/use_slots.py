# -*- coding: utf-8 -*-
__author__ = 'vincent'

from types import MethodType

class Student(object):
    # slots用来限制该class可以动态添加的属性,对继承的子类是不起作用的
    __slots__ = ('name', 'age', 'set_age', 'set_score')
    pass

s = Student()
s.name = 'Vincent'
print(s.name)

def set_age(self, age):
    self.age = age

# 给实例绑定方法(对另外一个实例是不起作用的)
s.set_age = MethodType(set_age, s)
s.set_age = 25

def set_score(self, score):
    self.score = score

Student.set_score = MethodType(set_score, Student)

class CollegeStudent(Student):
    # if __slots__ 存在,则子类实例允许定义的属性就是该slots加父类slots
    # __slots__ = ()
    pass

cs = CollegeStudent()
cs.gender = 'female'
print (cs.gender)
