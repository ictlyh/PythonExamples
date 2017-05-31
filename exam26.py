#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 利用递归方法求5!。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam26.py
@time: 2016/12/22 20:27
"""


def func(n):
    if n == 1:
        return 1
    else:
        return n * func(n - 1)


if __name__ == "__main__":
    print(func(5))
