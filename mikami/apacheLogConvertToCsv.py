# codinf : utf-8

import re
import sys
import os

# errorcheck

def errCheck_file(inFullPath):
	if os.access(inFullPath,os.F_OK) == True:
		return

	print("ERROR: " + inFullPath + " is not found")
	exit()

def errCheck_args(args):
	if len(args) == 3 and (args[2] == "access" or args[2] == "error"):
		return

	print("Format: python apacheLogConvertToCsv.py [filepath] [access/error]")
	exit()


errCheck_args(sys.argv)

inFullPath = sys.argv[1] ; errCheck_file(inFullPath)
inFileRead = open(inFullPath)
inFileName = os.path.basename(inFullPath)

outFilePath = "/tmp/"
outFullPath = outFilePath + inFileName  + '.csv'
outFileWrite = open(outFullPath,'w')

# access/error
value = sys.argv[2]
if value == "access":
	re1 = r'^(\S+) (\S+) (\S+) \[([^\]]+)\] "([A-Z]+) ([^ "]+)? HTTP/[0-9.]+" ([0-9]{3}) ([0-9]+|-)'
	re2 = r'\1,\2,\3,\4,\5,\6,\7,\8'

if value == "error":
	re1 = r'^(\[([^\]]+)\]) \[([^\]]+)\] \[([^\]]+)\] ([A-z0-9]+)+: (\S+)'
	re2 = r'\2,\3,\4,\5'

# main

line = inFileRead.readline().replace(",","")

while line:
	fline = re.sub(re1,re2,line)
	outFileWrite.write(fline)
	line = inFileRead.readline().replace(",","")

inFileRead.close()
outFileWrite.close()

print("Output: " + outFullPath)
