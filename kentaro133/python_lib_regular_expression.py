#! /usr/bin/env python
# encoding: UTF-8

import re

m = re.search('(P(yth|l)|Z)o[pn]e?', 'Python')

print m
print ""

mm = re.search('py(thon)', 'python')

print mm.group()
print ""
print mm.group(0)
print ""
print mm.group(1)
