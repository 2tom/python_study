# coding: UTF-8

# 辞書 key value
sales = {"tguchi": 200, "fkoji": 300, "dotinstall": 500}

print "sales"
print sales
print ""

print "tguchi's sales"
print sales["tguchi"]
print ""

# fkojiのvalueを変更
sales["fkoji"] = 800

# abcを追加
sales["abc"] = 1000

print "sales"
print sales
print ""

print "tguchi's key value"
print "tguchi" in sales
print ""

print "keys"
print sales.keys()
print ""

print "values"
print sales.values()
print ""

print "items"
print sales.items()
print ""
