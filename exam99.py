#!/usr/bin/env python
# encoding: utf-8

"""
@desc:
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam99.py
@time: 2016/12/28 19:49
"""


def func():
    fa = open("exam97.py", "r")
    fb = open("exam98.py", "r")
    a = fa.read()
    b = fb.read()
    fa.close()
    fb.close()
    l = list(a + b)
    print(l)
    l.sort()
    print(l)


if __name__ == "__main__":
    func()
