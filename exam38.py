#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 求一个3*3矩阵对角线元素之和。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam38.py
@time: 2016/12/23 18:38
"""


def func(matrix):
    s = 0
    for i in range(3):
        s += matrix[i][i]
    return s


if __name__ == "__main__":
    m = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    print(func(m))
