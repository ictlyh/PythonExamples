#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 打印出杨辉三角形（要求打印出10行如下图）。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam61.py
@time: 2016/12/25 18:48
"""


def func(n):
    lines = []
    lines.append([1])
    lines.append([1, 1])
    for i in range(2, n):
        line = []
        line.append(1)
        for j in range(1, i):
            line.append(lines[i - 1][j - 1] + lines[i - 1][j])
        line.append(1)
        lines.append(line)
    for line in lines:
        print(' '.join(str(num) for num in line))


if __name__ == "__main__":
    func(10)
