#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Apache access log parser
# options

import os
import sys
import re
import argparse
import elasticsearch

from datetime import datetime
from elasticsearch import Elasticsearch

# fileの存在確認
def is_file_check(file):
    if not os.access(file, os.F_OK):
        print "ERROR: '%s' does not exist" % (file)
        sys.exit(1)
    if not os.access(file, os.R_OK):
        print "ERROR: '%s' does not read" % (file)
        sys.exit(1)
    if os.path.isdir(file):
        print "ERROR: '%s' is directory" % (file)
        sys.exit(1)

# accessログフォーマット
def accessParser(file):
    fread = open(file)
    line = fread.readline()
    while line:
        fline = map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', line))
        max = len(fline) - 1
        for i in range(len(fline)):
            if max == i:
                print fline[i]
            else:
                print fline[i] + ',' ,

        line = fread.readline()
    fread.close()

def esPost(file, url):
    try:
        es = Elasticsearch([url])
    except:
        print "ERROR: '%s' does not connect" % (url)
        sys.exit(1)

    fread = open(file)
    line = fread.readline()
    cnt = 0

    while line:
        fline = map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', line))
        time = datetime.now()
        cnt += 1
        doc = {
            'ipaddr': fline[0],
            'userID': fline[1],
            'clientID': fline[2],
            'requestTime': fline[3],
            'request': fline[4],
            'statusCode': fline[5],
            'responseBodySize': fline[6],
            'referer': fline[7],
            'userAgent': fline[8],
            'timestamp': time,
          }
        res = es.index(index="test-index", doc_type='test-type', id=cnt, body=doc)
        print res
        line = fread.readline()

# errorログフォーマット
# T.B.D

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', help='elasticsearch url ex. http://localhost:9200', action='store', dest='es_url', required=False)
    parser.add_argument('-l', help='apache access log file path', action='store', dest='logfile', required=True)
    args = vars(parser.parse_args())

    accessLog = args['logfile']
    is_file_check(accessLog)
    if args['es_url']:
        esUrl = args['es_url']
        esPost(accessLog, esUrl)
    else:
        accessParser(accessLog)

    sys.exit(0)
