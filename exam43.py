#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 模仿静态变量(static)另一案例。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam43.py
@time: 2016/12/23 19:02
"""

class Num:
    nNum = 1
    def inc(self):
        self.nNum += 1
        print 'nNum = %d' % self.nNum

if __name__ == '__main__':
    nNum = 2
    inst = Num()
    for i in range(3):
        nNum += 1
        print 'The num = %d' % nNum
        inst.inc()