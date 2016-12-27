#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 连接字符串。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam84.py
@time: 2016/12/27 19:49
"""


def func():
    delimiter = ','
    mylist = ['Brazil', 'Russia', 'India', 'China']
    print delimiter.join(mylist)
    print delimiter.join(s for s in mylist)


if __name__ == "__main__":
    func()
