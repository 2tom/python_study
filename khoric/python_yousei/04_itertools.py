# coding: utf-8

import itertools

for x in itertools.chain('ABC',"123",[4,5,6]):
	print str(x)+"\n",

for x in itertools.combinations('ABCDE',2):
	print x,	
