# -*- coding: utf-8 -*-
__author__ = 'vincent'

class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

class RunnableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')

class CarnivorousMixIn(object):
    def eat(self):
        print('Eating meat...')


class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass