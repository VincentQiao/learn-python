# -*- coding: utf-8 -*-
__author__ = 'vincent'

import logging

def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
        # print('exception!', e)
main()
print('END')
