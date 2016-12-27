#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 循环输出列表
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam77.py
@time: 2016/12/27 19:09
"""


def func(s):
    for i in range(len(s)):
        print s[i]


if __name__ == "__main__":
    func(["man", "woman", "girl", "boy", "sister"])
