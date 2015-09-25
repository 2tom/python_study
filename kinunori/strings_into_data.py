# coding: UTF-8

a = 10
b = 1.123456789
c = "koba"
d = {"gou":200, "taki":500}

# 数値はdecimals %d, 小数点はfloatinff %f.文字列はstrings %s
print "age: %d" % a
print "price: %f" % b
print "name: %s" % c

# 10桁で表示させたい(足りない場合はスペースが入る)
print "age: %10d" % a

# 10桁で表示させたい(足りない場合は0でパディング
print "age: %010d" % a

# 小数点の桁数を指定させたい(この場合は2桁)
print "price: %.2f" % b

# 辞書型の中から表示させたい場合
print "sales: %(gou)d" % d

# 複数表示させたい場合
print "%d and %f" % (a, b)
print "%d and %f and %s" % (a, b, c)
