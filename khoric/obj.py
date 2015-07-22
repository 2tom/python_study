# coding: UTF-8

class User(object):
	def __init__(self, name):
		self.name = name
	def greet(self):
		print "my name is %s !" % self.name

bob = User("Bob")

print bob.name
print bob.greet()
