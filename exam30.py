#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam30.py
@time: 2016/12/22 20:45
"""


def func(num):
    tmp = num
    s = ''
    while tmp:
        s += chr(tmp % 10 + 48)
        tmp /= 10
    if int(s) == num:
        print(True)
    else:
        print(False)


def func2(num):
    s = str(num)
    for i in range(int(len(s) / 2)):
        if s[i] != s[-i - 1]:
            return False
    return True

if __name__ == "__main__":
    print(func2(100901))
