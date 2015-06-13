# -*- coding: utf-8 -*-
__author__ = 'Vincent'

import time

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print(time.strftime('%Y-%m-%d %H:%I:%M', time.localtime(time.time())))


