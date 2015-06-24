#! /usr/bin/python
# coding: UTF-8

import sys

print 5 + int("5")
print 5 + float("5")

age = 20
print "test " + str(age) + " test"	# int => str

# print "test " + age + " test"         # error!!
					# 文字列＋数字の場合はエラーになる

test=sys.argv[1]			# import sys &
					# 引数がないとエラーになる
print test

