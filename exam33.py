#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 按逗号分隔列表
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam33.py
@time: 2016/12/22 21:08
"""


def func(lists):
    return ','.join(str(l) for l in lists)


if __name__ == "__main__":
    print(func([1,2,3,4,5]))
