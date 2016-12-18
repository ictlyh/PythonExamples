#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 输入三个整数x,y,z，请把这三个数由小到大输出。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam5.py
@time: 2016/12/18 20:59
"""


def bubblesort(nums):
    n = len(nums)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if nums[j] >= nums[j + 1]:
                tmp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = tmp
    for num in nums:
        print num


def func():
    n = int(raw_input("input how many numbers:"))
    nums = []
    for i in range(0, n):
        nums.append(int(raw_input("number %d: " % (i + 1))))
    bubblesort(nums)


if __name__ == "__main__":
    func()
