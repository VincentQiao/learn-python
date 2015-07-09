# -*- coding: utf-8 -*-
__author__ = 'vincent'

from urllib import request, parse

url = 'https://api.douban.com/v2/book/2129650'
with request.urlopen(url) as f:
    data = f.read()
    print('Status', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))

# 模仿浏览器
# req = request.Request('http://www.kaolalicai.cn/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) '
#                              'AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 '
#                              'Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     data = f.read()
#     print('Status', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     # print('Data:', data.decode('utf-8'))
# # post, 登录weibo

print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')

login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])
req_login = request.Request('https://passport.weibo.cn/sso/login')
req_login.add_header('Origin', 'https://passport.weibo.cn')
req_login.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) '
                                   'AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 '
                                   'Mobile/10A5376e Safari/8536.25')
req_login.add_header('Referer', 'https://passport.weibo.cn/'
                                'signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
with request.urlopen(req_login, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

# 用代理访问(proxy)
# proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
# proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
# opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
# with opener.open('http://www.example.com/login.html') as f:
#     pass

# urllib提供的功能就是利用程序去执行各种HTTP请求。如果要模拟浏览器完成特定功能，需要把请求伪装成浏览器。
# 伪装的方法是先监控浏览器发出的请求，再根据浏览器的请求头来伪装，User-Agent头就是用来标识浏览器的
