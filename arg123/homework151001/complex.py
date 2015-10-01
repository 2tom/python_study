#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import argparse
import collections

# setting
conf_file = '/etc/httpd/conf/httpd.conf'
log_dir = 'input'
access_log = 'access_log'
error_log = 'error_log'
output_dir = 'output'
output_types = ['csv', 'tsv', 'ltsv', 'json']
extension = {
        'csv':'.csv',
        'tsv':'.tsv',
        'ltsv':'.ltsv',
        'json':'.json',
        }
delimiter_type = ['csv', 'tsv']
delimiter = {
        'csv':',',
        'tsv':'\t',
        }


def normal_spliter(string):
    ret = []
    unity = False
    buf = []
    for s in string:
        if s in ['"', '[', ']']:
            unity = not(unity)
            continue
        if s in (' ', '\n') and not unity:
            ret.append(''.join(buf))
            buf = []
        else:
            buf += s
    if buf:
        ret.append(''.join(buf))
    return ret


def error_log_spliter(string):
    def remove_scrap(orig):
        return orig.replace('[', '').replace('\n', '')

    ret = string.split('] ')
    ret = map(remove_scrap, ret)
    return ret


def quotation(s):
    if s.count(' ') > 0 or s.count(',') > 0:
        return '"' + s + '"'
    else:
        return s

def get_label(tag):
    labels = {
            '%t':'time',
            '%h':'host',
            '%{X-Forwarded-For}i':'forwardedfor',
            '%l':'ident',
            '%u':'user',
            '%r':'req',
            '%!414r':'req',
            '%m':'method',
            '%U':'uri',
            '%q':'uri',
            '%H':'protocol',
            '%>s':'status',
            '%B':'size',
            '%b':'size',
            '%I':'reqsize',
            '%{Referer}i':'referer',
            '%{User-agent}i':'ua',
            '%{User-Agent}i':'ua',
            '%{Host}i':'vhost',
            '%D':'reqtime_microsec',
            '%T':'reqtime',
            '%{X-Cache}o':'cache',
            '%{X-Runtime}o':'runtime',
            '-':'upptime',
            }
    if tag in labels:
        return labels[tag]
    else:
        return tag

def get_logformat():
    with open(conf_file, "r") as cf:
        lines = cf.readlines()
        for line in lines:
            if line.find("CustomLog") == 0:
                format_name =  normal_spliter(line)[2]
                break
        for line in lines:
            if line.find("LogFormat") == 0 and line.find(format_name) != -1:
                logformat =  line[line.find('"') + 1:line.rfind('"')].replace('\\"', '"')
                break
        return logformat

def convert(input_type, input_filename, input_format, output_filename, output_type, no_header):
    def spliter(s):
        if input_type == 'access':
            return normal_spliter(s)
        elif input_type == 'error':
            return error_log_spliter(s)

    with open(input_filename, 'r') as inf, open(output_filename, 'w') as outf:
        if not(no_header) or output_type not in delimiter_type:
            labels = [get_label(tag) for tag in normal_spliter(input_format)]
            if output_type in delimiter_type:
                outf.write(delimiter[output_type].join(labels) + '\n')
        for row in inf.readlines():
            if output_type in delimiter_type:
                buf = map(quotation, spliter(row))
                outf.write(delimiter[output_type].join(buf) + '\n')
            else:
                dic = collections.OrderedDict(zip(labels, spliter(row)))
                if output_type == 'json':
                    outf.write(json.dumps(dic) + '\n')
                if output_type == 'ltsv':
                    write_buffer = []
                    for k, v in dic.items():
                        write_buffer.append(k + ':' + v)
                    outf.write('\t'.join(write_buffer) + '\n')


def convert_access_log(**kwargs):
    input_type = 'access'
    input_format = get_logformat()
    input_filename = log_dir + os.sep + access_log
    output_filename = output_dir + os.sep + access_log + extension[kwargs['output_type']]
    convert(input_type, input_filename, input_format, output_filename, **kwargs)


def convert_error_log(**kwargs):
    input_type = 'error'
    input_format = 'time level message'
    input_filename = log_dir + os.sep + error_log
    output_filename = output_dir + os.sep + error_log + extension[kwargs['output_type']]
    convert(input_type, input_filename, input_format, output_filename, **kwargs)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '-o',
            '--output_type',
            dest='output_type',
            type=str,
            default='csv',
            choices=output_types,
            help='出力形式(デフォルト:csv)'
            )
    parser.add_argument(
            '--no_header',
            dest='no_header',
            action='store_true',
            help='csv/tsvのheaderを付けない場合に指定'
            )
    args = parser.parse_args()
    if args.output_type == 'json':
        global json
        import json

    convert_access_log(**vars(args))
    convert_error_log(**vars(args))


if __name__ == '__main__':
    main()
