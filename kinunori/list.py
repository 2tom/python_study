# coding: UTF-8
# リストに入れるのは同じ型でなくてもいい
sales = [255, 100, 353, 400]

# len + * []
print len(sales) #4が返ってくる

print sales[2] # 353

sales[2] = 100 # salesの[2]に100を置き換え

print sales[2]  # 100 

# inでリストに該当の値があるかどうか判定 真偽値

print 100 in sales # True
print 101 in sales # False

# rangeで連番を作ることも可能
# 0から9までの連番を作成
print range(10)

# 3から9までの連番を作成
print range(3, 10)

# 3から9までで２つ飛ばしの連番を作成
print range(3, 10, 2)