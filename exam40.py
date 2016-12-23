#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 将一个数组逆序输出。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam40.py
@time: 2016/12/23 18:53
"""


def func(nums):
    for n in nums:
        print n
    for i in range(len(nums) / 2):
        nums[i], nums[-i - 1] = nums[-i - 1], nums[i]
    for n in nums:
        print n


if __name__ == "__main__":
    func([1, 2, 3, 4, 5, 6])
    func([1, 2, 3, 4, 5])
