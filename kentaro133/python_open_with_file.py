#! /usr/bin/env python
# encoding: UTF-8

# with 文を使って
with open('ifcfg-eth0', "r") as ff:
    f_str = ff.read()

print "### 読み込んだファイルを標準出力(with文)"
print f_str
print ""
ff.close()


with open('ifcfg-eth0', 'a') as fff:
    fff_str = fff.write('\nIPV4_FAILURE_FATAL=yes\n')

with open('ifcfg-eth0', 'r') as fff:
    fff_str = fff.read()

print "### 追記したファイルを標準出力(with文)"
print fff_str
