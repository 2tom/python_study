# coding: UTF-8
# ループ処理(for) 

# salesというリストを定義
sales = [13, 3523, 31, 238]
# sumという変数を宣言
sum = 0

# sale の中に salesリストにある要素を１つづつ代入し、forの中の処理をループ
for sale in sales:
        # sumにsalesリストの要素を1づつ足していく
        sum += sale
# ループが終わったタイミングで処理をしたい場合はelseを使う
else:
	print sum

# リストを使わずに0から順番に処理をさせた場合は range() を使う
# range(10)の場合、0から9までが順番に i に代入される
for i in range(10):

    # continueを使うと if で条件一致した場合、処理がスキップされる
    if i == 3:
     continue
    
    # breakを使うと if で条件一致した場合、ループを抜ける
    if i == 6:
     break
    print i





