#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 找到年龄最大的人，并输出。请找出程序中有什么问题。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam78.py
@time: 2016/12/27 19:11
"""


def func():
    person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
    m = 'li'
    for key in person.keys():
        if person[m] < person[key]:
            m = key
    print('%s,%d' % (m, person[m]))


if __name__ == "__main__":
    func()
