#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 按相反的顺序输出列表的值。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam32.py
@time: 2016/12/22 21:06
"""


def func(lists):
    for i in range(len(lists)):
        print(lists[-i - 1])


if __name__ == "__main__":
    func([1,2,3,4,5])
