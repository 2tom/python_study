# coding: UTF-8

# 文字列にデータを組み込む
a = 10
b = 1.1231231
c = "test"
d = {"fkoji": 200, "dotinstall": 500}

print "a"
print a
print ""
print "b"
print b
print ""
print "c"
print c
print ""
print "d"
print d
print ""

print "a"
print "age: %d" % a
print ""

print "d 10桁"
print "age: %10d" % a
print ""

print "d 0埋め"
print "age: %010d" % a

print "price: %.2f" % b

print "price: %f" % b

print "name: %s" % c

print "sale: %(fkoji)d" % d

print ""

print "%d    %f" % (a, b)
