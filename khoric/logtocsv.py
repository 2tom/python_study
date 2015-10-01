#coding: UTF-8

import sys

argvs = sys.argv

log = argvs[1]

f = open(log,'r')
o = open("output.csv", "w")

for line in f:
    newline = line.replace(' ', ',')
    o.write(newline,)

f.close()
o.close()
