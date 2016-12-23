#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 求100之内的素数。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam36.py
@time: 2016/12/23 18:26
"""


def func(num):
    nums = range(0, num + 1)
    for i in range(2, num + 1):
        j = 2
        while i * j <= num:
            nums[i * j] = 0
            j += 1
    for i in range(2, num + 1):
        if nums[i] != 0:
            print i


if __name__ == "__main__":
    func(100)
