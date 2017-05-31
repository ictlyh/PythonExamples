#!/usr/bin/env python
# encoding: utf-8

"""
@desc:
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam91.py
@time: 2016/12/28 19:25
"""


import time


def func():
    print(time.ctime(time.time()))
    print(time.asctime(time.localtime(time.time())))
    print(time.asctime(time.gmtime(time.time())))


if __name__ == "__main__":
    func()
