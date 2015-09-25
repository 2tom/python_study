#! /usr/bin/env python
# encoding: UTF-8

import os
import sys

os.mkdir('test')
print os.listdir(".")
os.rmdir('test')
print ""

sys.exit(1)
