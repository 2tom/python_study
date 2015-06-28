# coding: UTF-8

class User(object):
	def __init__(self, name):
		self.name = name
	def greet(self):
		print "my name is %s!" % self.name

class SuperUser(User):
	def shout(self):
		print "%s is Super!" % self .name

cuda = User("Cuda")
nash = SuperUser("Nash")

cuda.greet()
nash.greet()
nash.shout()
