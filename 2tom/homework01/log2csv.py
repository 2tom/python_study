#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Apache access log parser
# options

import os
import sys
import re
import time
import argparse

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
def accessLogParser(file):
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

def elasticsearchParser(line):
    fline =  map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', line))
    time = datetime.now()
    document = {
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

    return document


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
        try:
            es = Elasticsearch([esUrl])
        except:
            print "ERROR: '%s' does not connect" % (esUrl)
            sys.exit(1)

        file = open(accessLog, 'r')
        st_results = os.stat(accessLog)
        st_size = st_results[6]
        file.seek(st_size)

        while 1:
            where = file.tell()
            line = file.readline().rstrip()
            if not line:
                time.sleep(1)
                file.seek(where)
            else:
                doc = elasticsearchParser(line)
                res = es.index(index="test-index", doc_type='test-type', body=doc)
                print res

    else:
        accessLogParser(accessLog)

    sys.exit(0)
