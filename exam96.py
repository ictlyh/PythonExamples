#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 计算字符串中子串出现的次数。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam96.py
@time: 2016/12/28 19:35
"""


def func():
    a = "hello, nice to meet you. Nice to meet you too"
    b = 'nice'
    print(a.lower().count(b.lower()))

if __name__ == "__main__":
    func()
