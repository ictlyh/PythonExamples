#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam19.py
@time: 2016/12/21 19:35
"""


def isperfect(num):
    s = 0
    for i in range(1, int(num / 2 + 1)):
        if num % i == 0:
            s += i
    if s == num:
        return True
    else:
        return False


if __name__ == "__main__":
    for i in range(1, 1001):
        if isperfect(i):
            print(i, 'is a perfect number')
