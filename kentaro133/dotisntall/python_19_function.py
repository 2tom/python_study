# conding: UTF-8


def hello(name, num):
    print "hello %s! " % name * num


def hello2(name, num):
    return "hello %s! " % name * num


def hello3(name, num=3):
    return "hello %s! " % name * num


hello("cuda", 3)
hello("nash", 4)
hello(num=5, name="chevy")

s = hello("tahoe", 2)
s = hello2("ram", 2)
print s

s = hello3("aaa")
print s
