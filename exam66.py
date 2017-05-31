#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 输入3个数a,b,c，按大小顺序输出。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam66.py
@time: 2016/12/26 19:40
"""


def func(a, b, c):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    print(a, b, c)


if __name__ == "__main__":
    func(1, 2, 3)
    func(3, 2, 1)
    func(1, 3, 2)
    func(3, 1, 2)
    func(2, 1, 3)
    func(2, 3, 1)
