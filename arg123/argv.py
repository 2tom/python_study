#!/usr/bin/env python
# coding:utf-8
import sys
print sys.argv[0]
try:
  print sys.argv[1]
except IndexError:
  print "引数がありません"
