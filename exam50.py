#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 输出一个随机数
@ref: https://docs.python.org/2/library/random.html
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam50.py
@time: 2016/12/24 20:23
"""


import random


def func():
    print random.randint(1, 10)
    print random.random()
    print random.uniform(1, 10)
    print random.choice('abcde')
    items = [1, 2, 3, 4, 5]
    random.shuffle(items)
    print items
    print random.sample([1, 2, 3, 4, 5], 2)


if __name__ == "__main__":
    func()
