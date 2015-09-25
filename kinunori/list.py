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

# sort, reverse, split, join

sales = [59, 200, 56, 2999]
# 要素の順番を逆にする
sales.reverse()
print sales

# 小さい順番に要素をソートする
sales.sort()
print sales

# 要素を大きい順番でソートする(sort,reverseの組み合わせ)
sales.sort()
sales.reverse()
print sales

# 文字列をリスト化する

d = "2015/6/11"

# 2015, 6, 11　とリスト化する
# split() では () に区切り文字を指定する
print d.split("/") # [2015, 16, 11]

a = ["a", "b", "c"]

# リストを文字列にする
# ""の中に繋げるときの文字、.join()の()にリスト名を指定する
print "-".join(a)
