# coding: utf-8

import time,datetime

now = time.localtime() 
print now

print time.strftime('%Y-%m-%d %H:%M:%S', now)

now2 = datetime.datetime.now()
print now2.isoformat()

nextyear = datetime.datetime(2016,1,1)
delta = nextyear - now2

print delta.days
