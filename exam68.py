#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam68.py
@time: 2016/12/26 20:06
"""


def func(nums, m):
    n = len(nums)
    if n == 0:
        return nums
    m %= n
    res = []
    for i in range(n - m, n):
        res.append(nums[i])
    for i in range(0,n - m):
        res.append(nums[i])
    return res


if __name__ == "__main__":
    print(",".join(str(num) for num in func([1, 2, 3, 4, 5, 6], 2)))
    print(",".join(str(num) for num in func([], 1)))
    print(",".join(str(num) for num in func([1, 2, 3, 4, 5, 6], 12)))
