# coding: UTF-8
# 辞書型データでforループをさせる

users = {"koba":200, "yuki":300, "taki":400}

# key と value を usersの辞書型データからそれぞれ代入する
for key, value in users.iteritems():
	# %s(文字型データのstrings)にkeyを代入、 %d(数値データのdecimal)にvalueを代入し標準出力
	print "key: %s value: %d" % (key, value)

# keyだけを対象とする
for key in users.iterkeys():
	# %s(文字型データのstrings)にkeyを代入、 %d(数値データのdecimal)にvalueを代入し標準出力
	print key

# valueだけを対象とする
for value in users.itervalues():
	# %s(文字型データのstrings)にkeyを代入、 %d(数値データのdecimal)にvalueを代入し標準出力
	print value
