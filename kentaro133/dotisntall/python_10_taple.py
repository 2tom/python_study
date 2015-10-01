# coding: UTF-8

# タプル　ー　値の変更を許さない
t = (2, 5, 8)
print t
print len(t)
print t * 3
# t[2] = 100
l = list(t)
print l
l[2] = 100
print l
tt = tuple(l)
print tt
