#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 一球从100米高度自由落下，每次落地后反跳回原高度的一半；
       再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam20.py
@time: 2016/12/21 19:41
"""


def func(h, c):
    dist = h
    for i in range(c - 1):
        dist += h
        h /= 2
    return dist, h / 2


if __name__ == "__main__":
    dist, h = func(100.0, 10)
    print('dist = %f, h = %f' % (dist, h))
