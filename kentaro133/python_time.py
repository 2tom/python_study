#! /usr/bin/env python
# encoding: UTF-8

import time
import datetime

now1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

print "time モジュール"
print now1
print ""

now2 = datetime.datetime.now()

print "datetime モジュール"
print now2.isoformat()
print ""
