#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 对10个数进行排序
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam37.py
@time: 2016/12/23 18:31
"""


def selectsort(nums):
    n = len(nums)
    for i in range(0, n):
        idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[idx]:
                idx = j
        nums[i], nums[idx] = nums[idx], nums[i]
    print ",".join(str(num) for num in nums)


if __name__ == "__main__":
    nums = [1, 3, 0, 9, 7, 5, 2, 7]
    selectsort(nums)
