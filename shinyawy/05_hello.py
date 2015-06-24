# coding: UTF-8
# No.1 Python Study 2015/06/11
# 文字列
# "hello" 'hello'
# 日本語 u"こんにちは！
# + *
# エスケープ \n \t \\
print "hello" + "world"
print u"無駄！"* 10
# 日本語の時はuを入れないといけない
# asciiとunicodeは混在できない
# お作法的な話：""は変える文字
# お作法的な話：''は変えない文字
print 'hello\n wo\trld\\ it\'s a pen'

print """<html lang="ja">
<body>
</body>
</html>"""