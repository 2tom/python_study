#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import os
import sys
import re
parser = argparse.ArgumentParser(description='Apacheのaccess_log(error_log)をcsvに変換するスクリプト')
parser.add_argument('-e', '--error_log', dest='error_log', action='store_true', help='error_logを変換する場合に指定')
parser.add_argument('filename', action='store', type=str, help='処理対象のファイル名')
args = parser.parse_args()
if not os.path.exists(args.filename):
    print 'ファイルがないがね'
    sys.exit(1)
if args.error_log:
    delimiter = '] '
else:
    delimiter = ' '
with open(args.filename, 'r') as f:
    for row in f.readlines():
        row = row.replace(delimiter, delimiter.replace(' ', ','))
        if not args.error_log:
            pat = r'[\[\"].+?[\]\"]'
            for s in re.findall(pat, row):
                row = row.replace(s, s.replace(',', ' '))
        print row,
