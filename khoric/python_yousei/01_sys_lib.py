# coding: utf-8

import sys

argvs = sys.argv
argc = len(argvs)
arg1 = sys.argv[1]
executable = sys.executable

# 引数の個数を出力
print argc

# 引数全てを出力
print argvs

# 1つ目の引数を出力
print arg1

# Python実行ファイル名を出力
print executable

sys.exit(1)
