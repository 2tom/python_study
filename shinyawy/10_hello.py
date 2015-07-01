# coding: UTF-8
# No.4 Python Study 2015/07/1
# タプル (変更できない)
a = (2, 5, 8)
# len + * []
# 3
print len(a)
print a * 3
# a[2] = 10 変更できない

# タプル <> リスト
b = list(a)
print b
c = tuple(b)
print c

# 使うタイミングは性能面やメモリを気にする時が多い
