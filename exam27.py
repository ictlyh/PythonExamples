#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam27.py
@time: 2016/12/22 20:30
"""


def func(s, i):
    print(s[i])
    if i == 0:
        return
    else:
        func(s, i - 1)


if __name__ == "__main__":
    func("abcdef", 4)
