# coding: UTF-8

# 辞書 key value
sales = {"tguchi":200, "fkoji":300, "dotinstall":500}

print sales

print sales["tguchi"]

sales["fkoji"] = 800

print sales

print "tguchi" in sales

print sales.keys()
print sales.values()
print sales.items()
