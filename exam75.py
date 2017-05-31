#!/usr/bin/env python
# encoding: utf-8

"""
@desc:
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam75.py
@time: 2016/12/26 20:32
"""


def func():
    for i in range(5):
        n = 0
        if i != 1:
            n += 1
        if i == 3:
            n += 1
        if i == 4:
            n += 1
        if i != 4:
            n += 1
        if n == 3:
            print(64 + i)


if __name__ == "__main__":
    func()