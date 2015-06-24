# coding: UTF-8
# 関数を使う

# 複数の処理をまとめて定義する

# def の次に関数名() を書いて、インデントをつけて処理を記述する
def hello():
	print "hello"

# 関数を呼ぶ時は 関数名() と書けばOK
hello()

# 引数を渡す場合は、()に引数を書く 初期値をつける場合は num = xとする
def kobaphone(name, num = 1):
	# 関数を呼び出された時に、呼び出した際の引数を name に代入して処理を実行
	print "プルプルプル %s" % name * num

def kobakaeri(name):
	# 返り値としたい場合は return をつけておく
        return "返り値は %s" % name 

# 引数に "もしもし" を渡して 関数kobaphoneを実行
# num に渡す引数を省略しているので初期値が入る
kobaphone("もしもし")

# 引数の 3 が num に代入されて、 処理が３回実行される
kobaphone("こんにちわ", 3)

# 引数に名前をつけて指定する
kobaphone(num = 2, name = "まぐろ")

# s に return の行にある処理が返り値として代入される
s = kobakaeri("これが返り値だ！")

# 返り値が代入された変数 s を出力
print s
