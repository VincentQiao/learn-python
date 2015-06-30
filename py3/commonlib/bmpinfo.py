# -*- coding: utf-8 -*-
__author__ = 'Vincent'

import struct


def bmpinfo(*args):
    name = args[0]
    with open(name, 'rb') as f:
        s = f.read(30)
        if len(s) >= 30:
            head = s[0:30]
            info = struct.unpack('<ccIIIIIIHH', head)
            if info[0] == b'B' and info[1] == b'M':
                print('BMP! Size: %s * %s. Color: %s' % (info[6], info[7], info[2]))
                return
    print('Not BMP!')
    return

if __name__ == '__main__':
    # Windows environment
    bmpinfo('C:\\Users\\Vincent\\Desktop\\001.bmp')
    bmpinfo('C:\\Users\\Vincent\\Desktop\\empty.txt')