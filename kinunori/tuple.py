# coding: UTF-8
# タプルは要素の中身が変更できない配列

a = (2, 5, 8)

print len(a)
print a * 3
print a[2] + 2

# 要素が変更できないのでエラる
#a[2] = 10


#️ tuble <> List の変換
b = list(a)

print b

c = tuple(b)

print c