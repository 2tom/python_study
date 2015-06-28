# coding: UTF-8

# セット　ー　重複を許さない
ss = set([1, 2, 3, 4])
print ss
sss = set([1, 2, 3, 4, 3, 2])
print sss
ssss = set([3, 4, 5])
print ssss
print sss - ssss
print sss | ssss
print sss & ssss
print sss ^ ssss

