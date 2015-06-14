# -*- coding: utf-8 -*-
__author__ = 'vincent'


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.gender = None

    def gender(self, gender):
        self.gender = gender

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'



