#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 求1+2!+3!+...+20!的和。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam25.py
@time: 2016/12/21 20:10
"""


def func(n):
    s = 0
    m = 1
    for i in range(1, n + 1):
        m *= i
        s += m
    return s


if __name__ == "__main__":
    print(func(20))
