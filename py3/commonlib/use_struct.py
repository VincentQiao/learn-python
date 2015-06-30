# -*- coding: utf-8 -*-
__author__ = 'Vincent'

import struct
struct.pack('>I', 10240099)
struct.pack('>I', 4042322160)
struct.unpack('>I',struct.pack('>I', 10240099))
print(struct.unpack('>IIH', b'\x00\x9c@c\xf0\xf0\xf0\xf0\x80\x80'))