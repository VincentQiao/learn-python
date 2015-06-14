# -*- coding: utf-8 -*-
__author__ = 'vincent'

# get from Michale Liao's github:
# https://github.com/michaelliao/learn-python3/blob/master/samples/oop_basic/animals.py

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()

class Timer():
    def run(self):
        print('Start...')

a = Animal()
d = Dog()
c = Cat()
t = Timer()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

run_twice(c)

# 动态语言的鸭子类型.不要求严格的继承体系,一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
run_twice(t)

isinstance(a, Animal)
isinstance(a, Dog)
isinstance(d, Animal)
isinstance(d, Cat)
isinstance(d, (Dog, Cat))
try:
    isinstance(d, [Dog, Cat])
except TypeError:
    print('isinstance() arg 2 must be a type or tuple of types')
