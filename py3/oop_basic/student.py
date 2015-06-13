# -*- coding: utf-8 -*-
__author__ = 'vincent'


class Student(object):

    def __init__(self, name):
        self.name = name
        self.gender = None

    def gender(self, gender):
        self.gender = gender

