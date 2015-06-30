# -*- coding: utf-8 -*-
__author__ = 'Vincent'

from datetime import datetime, timedelta, timezone

# 获得当前时间的datetime
now = datetime.now()
print('now is =', now)
print('type(now) =', type(now))

# 创建datetime对象
dt = datetime(2015, 6, 30, 9, 38)
print('dt =', dt)

# datetime 对象转化为timestamp
print('datetime -> timestamp:', dt, '->', dt.timestamp())

# timestamp转化为datetime
t = dt.timestamp()
print('timestamp -> datetime:', datetime.fromtimestamp(t))
print('timestamp -> datetime as UTC+0:', datetime.utcfromtimestamp(t))


# str转化为datetime
cday = datetime.strptime('2015/06/30 9:45', '%Y/%m/%d %H:%M')
print('str -> datetime:', cday)

# datetime转为str
print('datetime -> str:', cday.strftime('%Y~~%m~%d..%H:%M'))

# 时间加减
now = datetime.now()
print('now:', now)
print('now + 8 hours:', now+timedelta(hours=8))
print('now - 3 days:', now-timedelta(days=3))
print('now + 3 days, 2 hours', now+timedelta(days=3, hours=2))

# 本地时间转换为UTC时间
tz_utc_8 = timezone(timedelta(hours=8))



