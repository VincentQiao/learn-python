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


# TODO: print log before and after func()
def logger(ins):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("begin call")
            res = func(*args, **kw)
            print("end call")
            return res
        return wrapper
    if callable(ins):
        return decorator(ins)
    else:
        print(ins)
        return decorator


@logger
def now1():
    print("2015")


@logger("hello world")
def now2():
    print("2015")

now2()
now2()