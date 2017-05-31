#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 输出9*9乘法口诀表。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam8.py
@time: 2016/12/19 21:11
"""


def multiply():
    for i in range(1, 10):
        for j in range(1, 10):
            print('%d * %d = %d' % (i, j, i * j))
        print('')


if __name__ == "__main__":
    multiply()
