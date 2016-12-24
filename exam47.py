#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 两个变量值互换。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam47.py
@time: 2016/12/24 20:15
"""


def func(a, b):
    print 'a = ', a, 'b = ', b
    a, b = b, a
    print 'a = ', a, 'b = ', b


if __name__ == "__main__":
    func(1, 2)
    func("hello", "world")
    func([1, 2, 3], [4, 5, 6])
    func({1:1, 2:2}, {3:3, 4:4})

