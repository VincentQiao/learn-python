# -*- coding: utf-8 -*-
__author__ = 'vincent'

from urllib import request

url = 'https://api.douban.com/v2/book/2129650'
with request.urlopen(url) as f:
    data = f.read()
    print('Status', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))