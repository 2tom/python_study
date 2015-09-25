# coding: UTF-8
# 文字列
# 文字列 len
# 検索 find
# 切り出し [] [start:end]

import sys

s = "abcdefghijk"

print len(s)
print s.find("k")



print s[-2]

# 数値 <> 文字列

# 文字列 -> 数値 int float
# 数値 -> 文字列 str

print 5 + float("5")
print 5 + int("5")


#age = 20 

age = sys.argv[1]
print "i am " + str(age) + " years old!" 
