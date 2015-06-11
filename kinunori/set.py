# coding: UTF-8
# セット(集合型) - 重複を許さない

a = set([1,2,3,4])
b = set([3,4,5])

print a
print b

# a　と b の差集合を表示(aにあってbにないもの)

print a - b # set([1, 2])

# 和集合の場合は | を使う(or)
 
print a | b # set([1, 2, 3, 4, 5])

# 積集合の場合は & を使う(and)

print a & b # set([3, 4])

# !andの場合は ^ を使う

print a ^ b # set([1, 2, 5])