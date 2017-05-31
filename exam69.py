#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），
       凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam69.py
@time: 2016/12/26 20:14
"""


def func(n):
    num = []
    for i in range(n):
        num.append(i + 1)
    i = 0
    k = 0
    m = 0
    while m < n - 1:
        if num[i] != 0:
            k += 1
        if k == 3:
            num[i] = 0
            k = 0
            m += 1
        i += 1
        if i == n:
            i = 0
    i = 0
    while num[i] == 0:
        i += 1
    print(num[i])


if __name__ == "__main__":
    func(34)
