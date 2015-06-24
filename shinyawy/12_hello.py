# coding: UTF-8
# No.? Python Study 2015/07/?
# 辞書 key value
# [2505, 532, 500]
sales = {"taguchi":200, "fkoji":300, "dotinstall":500}
print sales
print sales["taguchi"]
sales["fkoji"] = 800
print sales
# in
print "taguchi" in sales # True
#keys, values, items
print sales.keys()
print sales.values()
print sales.items()