#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
       假如兔子都不死，问每个月的兔子总数为多少？
       f(n + 1) = f(n) + f(n-1)
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam11.py
@time: 2016/12/20 19:35
"""


def func(n):
    if n <= 2:
        return 1
    elif n == 3:
        return 2
    else:
        return func(n - 1) + func(n - 2)

if __name__ == "__main__":
    for i in range(1, 20):
        print(func(i))

