# coding: UTF-8

# 文字列を x 3 にして結合してreturn
def hello(name, num = 3):
	return "hello %s !" % name * num

s=hello("tom")
print s

q=hello(name="hori", num=2)
print q
