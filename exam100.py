#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 列表转换为字典
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam100.py
@time: 2016/12/28 19:56
"""


def func():
    a = [1, 2]
    b = ['a', 'b']
    c = [(1, 2, 3), (4, 5, 6)]
    print a, b, c
    d = dict([a, b, c])
    print d


if __name__ == "__main__":
    func()
