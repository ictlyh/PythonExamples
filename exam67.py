#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam67.py
@time: 2016/12/26 19:49
"""


def func(nums):
    print ','.join(str(num) for num in nums)
    minidx = 0
    maxidx = 0
    for i in range(len(nums)):
        if nums[i] < nums[minidx]:
            minidx = i
    nums[minidx], nums[len(nums) - 1] = nums[len(nums) - 1], nums[minidx]
    for i in range(len(nums)):
        if nums[i] > nums[maxidx]:
            maxidx = i
    nums[maxidx], nums[0] = nums[0], nums[maxidx]
    print ','.join(str(num) for num in nums)


if __name__ == "__main__":
    func([1, 2, 3, 4, 5])
    func([5, 4, 3, 2, 1])
    func([1, 4, 2, 5, 3])
