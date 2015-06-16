# -*- coding: utf-8 -*-
__author__ = 'vincent'



try:
    print('try...')
    r = 10/int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')