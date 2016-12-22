#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 练习函数调用。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam34.py
@time: 2016/12/22 21:09
"""

# 可以看到 python 函数可以先调用后定义
def a():
    print 'calling b'
    b()


def b():
    print 'calling c'
    c()


def c():
    print 'c'


if __name__ == "__main__":
    a()
