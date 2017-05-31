#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam39.py
@time: 2016/12/23 18:41
"""


def func(nums, num):
    n = len(nums)
    nums.append(0)
    if nums[n - 1] <= num:
        nums[n] = num
    else:
        for i in range(n):
            if nums[i] >= num:
                for j in range(n, i, -1):
                    nums[j] = nums[j - 1]
                nums[i] = num
                break
    for n in nums:
        print(n)


if __name__ == "__main__":
    func([1, 2, 4, 5], 3)
    func([1, 2, 3, 4], 5)
    func([2, 3, 4, 5], 1)
