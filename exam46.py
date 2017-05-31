#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 求输入数字的平方，如果平方运算后小于 50 则退出
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam46.py
@time: 2016/12/24 20:12
"""


def func(nums):
    for num in nums:
        if num ** 2 < 50:
            break
        print(num ** 2)


if __name__ == "__main__":
    func([9, 8, 7, 6, 5])
