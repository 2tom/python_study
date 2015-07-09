#! /usr/bin/env python
# encoding: UTF-8

# 読み取りモードでファイルオープン
f = open('ifcfg-eth0', 'r')

print "### 読み込んだファイルを標準出力に表示"
print f.read()
print ""

# close メソッドを使って、ファイルを閉じる
f.close()

# 書き込みモードでファイルオープン
f = open('ifcfg-eth0', 'a')

# 書き込みして、一旦クローズ
f.write('IPV6INIT=no')
f.close()

# 読み取りモードで開きなす
f = open('ifcfg-eth0', 'r')
print "### 追記したファイルを標準出力に表示"
print f.read()
print ""
