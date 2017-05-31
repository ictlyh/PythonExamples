#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 时间函数举例
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam92.py
@time: 2016/12/28 19:26
"""


import time


def func():
    start = time.time()
    for i in range(3):
        print(i)
        time.sleep(1)
    end = time.time()
    print(end - start)


if __name__ == "__main__":
    func()
