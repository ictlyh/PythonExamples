#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 求0—7所能组成的奇数个数。（9位数以内）
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam83.py
@time: 2016/12/27 19:43
"""


def func():
    sum = 4
    s = 4
    for j in range(2, 9):
        if j <= 2:
            s *= 7
        else:
            s *= 8
        sum += s
    print 'sum = %d' % sum


if __name__ == "__main__":
    func()
