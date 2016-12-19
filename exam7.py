#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 将一个列表的数据复制到另一个列表中。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam7.py
@time: 2016/12/19 21:09
"""


def listcopy(nums):
    backup = []
    for num in nums:
        backup.append(num)
    return backup


if __name__ == "__main__":
    a = [1, 2, 3, 4]
    for num in a:
        print num;
    b = listcopy(a)
    for num in b:
        print num
