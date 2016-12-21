#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam24.py
@time: 2016/12/21 20:06
"""


def func():
    a = 2.0
    b = 1.0
    s = 0;
    for i in range(20):
        s += (a / b)
        a, b = a + b, a
    print s


if __name__ == "__main__":
    func()
