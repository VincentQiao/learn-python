# -*- coding: utf-8 -*-
__author__ = 'vincent'


# Python itself has no mechanism to stop you to do bad things, you have to watch yourself from doing that.
# Even if you use self.__score to present a private variable, Python just change the name of the variable
# to self.__Student__score or something like that, which you can still access to and change by yourself through
# an instance
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        self.__gender = None

    def gender(self, gender):
        self.__gender = gender

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad value')

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'
