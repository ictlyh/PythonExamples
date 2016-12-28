#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 结构体变量传递
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam87.py
@time: 2016/12/28 19:02
"""


class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def set(self, a, b):
        self.x = a
        self.y = b

    def show(self):
        print '%d,%d' % (self.x, self.y)


if __name__ == "__main__":
    p = Point()
    p.show()
    p.set(1, 2)
    p.show()
