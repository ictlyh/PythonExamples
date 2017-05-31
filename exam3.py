#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam3.py
@time: 2016/12/18 20:44
"""

import math


def func():
    for i in range(1, 10000):
        x = int(math.sqrt(i + 100))
        y = int(math.sqrt(i + 268))
        if x * x == (i + 100) and y * y == (i + 268):
            print('num = ', i)


if __name__ == "__main__":
    func()
