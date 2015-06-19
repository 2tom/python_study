# coding: UTF-8
# 条件分岐 if
# 比較演算子 > < >= <= == !=
# 論理演算子 and or not

score = 45
if 60 < score < 80:
	print "ok!"
	print "OK!"
elif score > 40:
	print "soso..."
else:
	print "NG!"

print "OK!" if score > 60 else "NG!!!!!"