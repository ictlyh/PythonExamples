#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 创建一个链表
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam72.py
@time: 2016/12/26 20:25
"""


def func():
    lists = []
    for i in range(5):
        lists.append("hello" + str(i))
    print(",".join(s for s in lists))


if __name__ == "__main__":
    func()
