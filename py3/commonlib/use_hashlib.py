# -*- coding: utf-8 -*-
__author__ = 'Vincent'

# 摘要算法，哈希算法
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

def get_md5(password):
    md5_password = hashlib.md5()
    md5_password.update(password.encode('utf-8'))
    return md5_password.hexdigest()

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
db['vincent'] = get_md5('hiqiao')

def login(user, password):
    if db[user] == get_md5(password):
        return True
    elif db[user] == get_md5(password+user+'the-Salt'):
        return True
    return False

login('vincent', 'hiqiao')

def register(username, password):
    db[username] = get_md5(password+username+'the-Salt')
