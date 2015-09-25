# coding: UTF-8
# オブジェクト（変数と関数をまとめたもの）
# クラス：オブジェクトの設計図
# インスタンス：クラスを実体化したもの
class User(object):
    def __init__(self, name):
        self.name = name
    def greet(self):
        print "my name is %s!" % self.name

bob = User("Bob")
tom = User("Tom")
print bob.name
bob.greet()
tom.greet()
