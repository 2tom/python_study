# coding: UTF-8
# No.4 Python Study 2015/07/1
# 辞書 key value
# [2505, 532, 500]
sales = {"taguchi":200, "fkoji":300, "dotinstall":500}
print sales
print sales["taguchi"]
sales["fkoji"] = 800
print sales

# in
# True
print "taguchi" in sales
#keys, values, items
print sales.keys()
print sales.values()
print sales.items()