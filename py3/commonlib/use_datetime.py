# -*- coding: utf-8 -*-
__author__ = 'Vincent'

import re
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
now = datetime.now()
dt = now.replace(tzinfo=tz_utc_8)
print('now:', now)
print('time utc-8:', dt)

# 时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print('utc-dt:', utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('bj_dt:', bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
tokyo2_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))
print('tokyo_dt:', tokyo_dt)
print('tokyo_dt2:', tokyo_dt)


def to_timestamp(dt_str, tz_str):
    hour = int(re.compile(r'UTC(.\d+?):').findall(tz_str)[0])
    here_dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    out_dt = here_dt.replace(tzinfo=timezone(timedelta(hours=hour)))
    return out_dt.timestamp()

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')
