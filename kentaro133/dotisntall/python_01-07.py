# coding: UTF-8

# 標準出力
print "hello world"
print

# 変数
msg = "hello world"
print msg
print ""

# 数値
print 10 * 5  # 50
print 10 // 3  # 3
print 10 % 3  # 1
print 2 ** 3  # 8
print ""

# 整数と小数
print 5 + 2.0  # 7.0
print 10 / 3  # 3
print 10 / 3.0  # 3.33
print ""

# 文字列
print "hello" + "world"
print u"無駄！" * 10
print 'hello\n wo\trld it\'s a pen'
print """<html lang="ja">
<body>
</body>
</html>"""
print ""

# 文字列操作
s = "abcdefghijk"
print len(s)
print s.find("f")
print s[0]
print s[2:5]
print s[:5]
print s[5:]
print s[2:-1]
print ""

# 文字列・数値変換
print 5 + int("5")
print 5 + float("5")
age = 10
print "i am " + str(age) + " years old!"
print ""
