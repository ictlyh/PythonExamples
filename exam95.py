#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 字符串日期转换为易读的日期格式。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam95.py
@time: 2016/12/28 19:35
"""

from dateutil import parser


def func():
    dt = parser.parse("Aug 28 2015 12:00AM")
    print(dt)


if __name__ == "__main__":
    func()
