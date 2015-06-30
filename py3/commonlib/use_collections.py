# -*- coding: utf-8 -*-
__author__ = 'Vincent'

from collections import namedtuple, deque, defaultdict, OrderedDict, Counter, Iterator, Iterable
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
q.pop()
print(q)

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'value1'

d = dict([('a', 1), ('b', 2), ('c', 3)])
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
od['z'] = 1
od['y'] = 2
od['x'] = 3

# 实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
class LastUpdateOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdateOrderedDict, self).__init__()
        # OrderedDict.__init__(self)
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        # dict容量达到上限
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False) # last=False, 表示弹出dict首部的元素
            print('remove:', last)
        if containsKey:
            del self[key] # 有必要吗？
            print('set:', (key, value))
        else:
            print('add:', key, value)
        OrderedDict.__setitem__(key, value)

c = Counter()
for ch in 'Programming':
    c[ch] = c[ch] + 1