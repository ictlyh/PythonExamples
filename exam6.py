#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 斐波那契数列
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam6.py
@time: 2016/12/19 21:05
"""


def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


if __name__ == "__main__":
    print(fibonacci(10))
