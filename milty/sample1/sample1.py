#!/usr/bin/env python
# coding: UTF-8

import sys

'''
  ＠ 'ェ' ＠
'''

class Sample1(object):
    def notmagic(self):
        print '-10<int> /[floor]     3.0<float> => -3.3333<float> : %.4f<float>' % (-10/3.0)
        print '+10<int> //[floordiv] 3.0<float> => floor( 3.3333<float>) =>  3.0000 : %.4f<float>' % (10//3.0)
        print '-10<int> //[floordiv] 3.0<float> => floor(-3.3333<float>) => -4.0000 : %.4f<float> ' % (-10//3.0)
        sys.stdout.flush()


if __name__ == '__main__':
    app = Sample1()
    app.notmagic()
