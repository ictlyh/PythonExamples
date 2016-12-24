#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 取一个整数a从右端开始的4〜7位。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam54.py
@time: 2016/12/24 20:38
"""


def func(n):
    a = 0X0F
    print (n >> 4) & a


if __name__ == "__main__":
    func(0XF0)
    func(0XB0)
    func(0XA0)
    func(0X70)
