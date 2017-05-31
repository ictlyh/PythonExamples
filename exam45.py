#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 统计 1 到 100 之和。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam45.py
@time: 2016/12/23 19:10
"""


def func():
    s = 0
    for i in range(100):
        s += i + 1
    print(s)


if __name__ == "__main__":
    func()