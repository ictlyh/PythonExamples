#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 两个变量值互换。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam48.py
@time: 2016/12/24 20:18
"""


def func(a, b):
    if a < b:
        print(a, '<', b)
    elif a == b:
        print(a, '=', b)
    else:
        print(a, '>', b)


if __name__ == "__main__":
    func(1, 2)
    func('a', 'b')
    func([4, 5, 7], [4, 5, 6])
