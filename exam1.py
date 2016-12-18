#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam1.py
@time: 2016/12/18 20:18
"""


def func():
    numbers = []
    counts = 0
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if i != j and j != k and k != i:
                    numbers.append([i, j, k])
                    counts += 1
    return counts, numbers


if __name__ == "__main__":
    count, items = func()
    print 'count = ', count
    for item in items:
        print item
