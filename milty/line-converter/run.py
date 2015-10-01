#!/usr/bin/env python
# -*- coding: utf-8 -*-

### functions
inputEncoding = 'utf8'
outputEncoding = 'utf8'

def sprintf(*args, **kwargs):
    return kwargs.get('fmt', '{0}').format(*args) \
    .decode(kwargs.get('decode', inputEncoding)).encode(kwargs.get('encode', outputEncoding))


def printf(*args, **kwargs):
    try:
        print '{0}'.format(sprintf(*args, **kwargs))
    except UnicodeError as e:
        """ windowsかもしれんのでcp932を試してみよう(まあ化けるかもしれないが) """
        print '{0}'.format(sprintf(*args, decode='cp932', encode='cp932', **kwargs))


### Awesome object oriented designed converters
class NoDriverException(Exception):
    pass

class Converter():
    def convert(self, str, **kwargs):
        raise NoDriverException("これはインターフェースなので何もしない")
        
class CSVConverter(Converter):
    def convert(self, str, **kwargs):
        return ','.join(str.split())

class TSVConverter(Converter):
    def convert(self, str, **kwargs):
        return '\t'.join(str.split())

class AwesomeConverter(Converter):
    CSV = 'csv'
    TSV = 'tsv'
    
    def __init__(self):
        self.CSVDriver = None
        self.TSVDriver = None
    
    """ 頭ひねると「なんちゃらせぱれーとばりゅー」は実はコレでできる(','を書き換えればTabSVでも_SVでも) """
    def convert(self, str, **kwargs):
        __driver = kwargs.get('engine', AwesomeConverter.CSV).lower()
        if __driver in (AwesomeConverter.CSV, 'csv'):
            if self.CSVDriver is None:
                self.CSVDriver = CSVConverter()
            return self.CSVDriver.convert(str)
        elif __driver in (AwesomeConverter.TSV, 'tsv'):
            if self.TSVDriver is None:
                self.TSVDriver = TSVConverter()
            return self.TSVDriver.convert(str)
        else:
            raise NoDriverException("そんなConverterあるわけないだろ(´・ω・) => {0}".format(__driver))


""" 引数処理 """
import argparse

silentMode = False
engine = ''

""" 当然だけど引数処理終わるまではエンコードはUTF8だから """
try:
    parser = argparse.ArgumentParser(
        description=sprintf('標準入力にわたってくる文字列を行単位で逐次CSVに変換するよ！'))
    parser.add_argument(
        '--noheader',
        action='store_true',
        default=False,
        help=sprintf('余計なものを表示したくない場合'))
    parser.add_argument(
        '--engine',
        default=AwesomeConverter.CSV,
        help=sprintf(
          AwesomeConverter.CSV,
          AwesomeConverter.TSV,
          fmt='変換エンジンを指定できます({0}, {1})'))
    parser.add_argument(
        '--input-encoding',
        default='utf8',
        help=sprintf('入力するデータのエンコーディングを変更します'))
    parser.add_argument(
        '--output-encoding',
        default='utf8',
        help=sprintf('出力するデータのエンコーディングを変更します'))
    args = parser.parse_args()
    silentMode = vars(args)['noheader']
    engine = vars(args)['engine']
    inputEncoding = vars(args)['input_encoding']
    outputEncoding = vars(args)['output_encoding']
except Exception as e:
    printf(e, fmt='(´・ω・)ﾅﾝｼﾞｬｺﾚ…… > {0}')


""" こういう風に使うんだぜ(コメント外して実行してみよう)
printf("[おまけ]")
a = CSVConverter()
b = TSVConverter()
c = AwesomeConverter()
printf(a.convert("hoge- fuga- "))
printf(b.convert("hoge- fuga- "))
printf(c.convert("hoge- fuga- "))
printf(c.convert("hoge- fuga- ", engine=c.TSV))
printf(c.convert("hoge- fuga- ", engine=AwesomeConverter.CSV))
try:
    printf(c.convert("hoge- fuga- ", engine='超絶イカした無敵コンバータ'))
except Exception as e:
    printf(e)
printf("")
"""

import sys

if sys.stdin.isatty():
    if silentMode is False:
        printf('× データが何も入ってきておらぬようじゃな(・ω・) 標準出力に何かを流し込むべし！')
    sys.exit(1)

if silentMode is False:
    printf('--------------------------------------------------------------------------------')
    printf('(・ω・)ノ こんばーてぃんぐなう')
    printf('--------------------------------------------------------------------------------')
ac = AwesomeConverter()
try:
    for line in iter(sys.stdin.readline, ""):
        printf(ac.convert(line, engine=engine))
except (IOError, KeyError) as e:
    printf(e, fmt='ﾅﾝﾃﾞｽｯﾃ...(゜Д゜) > {0}')
except Exception as e:
    printf(e, fmt='(´・ω・)ﾅﾝｼﾞｬｺﾚ…… > {0}')

"""
  入力が tail -f とかでCTL-Cでそっちを止めるとこのプロセスもぶち殺されるので、この下の処理は
  意味が無くなることに注意しよう
  (それを補足するならちゃんとSubprocessとかシグナル制御するようなまともな設計にしないとね)
"""
if silentMode is False:
    printf('--------------------------------------------------------------------------------')
    printf('(´・ω・)ノ 終わりマスタ')
