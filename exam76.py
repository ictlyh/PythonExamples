#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,
       当输入n为奇数时，调用函数1/1+1/3+...+1/n(利用指针函数)
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam76.py
@time: 2016/12/27 19:05
"""


def peven(n):
    i = 0
    s = 0.0
    for i in range(2, n + 1, 2):
        s += 1.0 / i
    return s


def podd(n):
    s = 0.0
    for i in range(1, n + 1, 2):
        s += 1.0 / i
    return s


def dcall(fp, n):
    s = fp(n)
    return s


if __name__ == "__main__":
    print dcall(peven, 6)
    print dcall(podd, 5)
