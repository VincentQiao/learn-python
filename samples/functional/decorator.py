# -*- coding: utf-8 -*-
__author__ = 'Vincent'

import time
import functools


def log_simple(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log_simple
def now():
    print(time.strftime('%Y-%m-%d %H:%I:%M', time.localtime(time.time())))


def log_text(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s()' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log_text('hello')
def new_now():
    print(time.strftime('%Y-%m-%d %H:%I:%M', time.localtime(time.time())))


def log(arg):
    # arg is not text, it's a func name
    if not isinstance(arg, str):
        @functools.wraps(arg)
        def wrapper(*args, **kw):
            print('call %s()' % arg.__name__)
            return arg(*args, **kw)
        return wrapper
    # arg is text
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s()' % (arg, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator


@log
def f1():
    pass


@log('hello')
def f2():
    pass

