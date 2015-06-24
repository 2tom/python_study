# coding: UTF-8

# 辞書は、Key value形式

sales = {"koba":200, "gou":300, "taki":500}
print sales["koba"] # 200

# 辞書に追加することもできる
sales["yuki"] = 400

# 辞書のvalueを変更する
sales["koba"] = 150
print sales["koba"] # 150

# key valueを全て表示
print sales

# salesのデータ内にkeyがあるかどうか判定
print "gou" in sales # true

# keyのみ表示
print sales.keys() 

# valueのみ表示
print sales.values()

# itemのみ表示
print sales.items() # [('gou', 300), ('taki', 500), ('koba', 150), ('yuki', 400)]




