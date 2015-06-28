# coding: UTF-8

def double(x):
	return x * x

print map(double, [2, 6, 9])

print map(lambda x:x * x, [3, 5, 7])