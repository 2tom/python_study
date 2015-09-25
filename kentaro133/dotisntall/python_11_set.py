# coding: UTF-8

# セット　ー　重複を許さない
ss = set([1, 2, 3, 4])
print ss

sss = set([1, 2, 3, 4, 3, 2])

print "sss"
print sss
ssss = set([3, 4, 5])

print "ssss"
print ssss

print "差集合"
print sss - ssss
print "和集合"
print sss | ssss
print "積集合"
print sss & ssss
print "!and"
print sss ^ ssss
