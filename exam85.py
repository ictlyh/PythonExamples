#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 判断一个素数能被几个9整除。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam85.py
@time: 2016/12/27 19:50
"""


def func(prime):
    val = 9
    n = 1
    while True:
        if val % prime == 0:
            break
        val = val * 10 + 9
        n += 1
    print "%d %% %d == 0" % (val, prime)

if __name__ == "__main__":
    func(3)
    #func(5)
    func(7)
