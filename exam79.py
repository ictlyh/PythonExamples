#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 字符串排序
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam79.py
@time: 2016/12/27 19:13
"""


def bubblesort(strs):
    for s in strs:
        print s
    n = len(strs)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if strs[j] >= strs[j + 1]:
                tmp = strs[j]
                strs[j] = strs[j + 1]
                strs[j + 1] = tmp
    for s in strs:
        print s


if __name__ == "__main__":
    bubblesort(['abcde', 'efdis', 'adk'])
