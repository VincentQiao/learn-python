# -*- coding: utf-8 -*-
__author__ = 'Vincent'

import base64
b64 = base64.b64encode(b'binary\x00string')
print(b64)
b = base64.b64decode(b64)
print(b)

def safe_base64_decode(s):
    mod = len(s) % 4
    if mod != 0:
        for i in range(4-mod):
            s += b'='
    return base64.b64decode(s)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')