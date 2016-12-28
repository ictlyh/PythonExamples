#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 时间函数举例3
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam93.py
@time: 2016/12/28 19:29
"""


import time


def func():
    start = time.clock()
    for i in range(10000):
        print i
    end = time.clock()
    print 'different is %6.3f' % (end - start)


if __name__ == "__main__":
    func()
