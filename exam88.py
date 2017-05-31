#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam88.py
@time: 2016/12/28 19:08
"""


def func(nums):
    for num in nums:
        print('*' * num)


if __name__ == "__main__":
    func([1, 2, 3, 4, 5, 6, 7])
