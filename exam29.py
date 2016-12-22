#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam29.py
@time: 2016/12/22 20:36
"""

def func(num):
    c = 0
    digits = []
    while num:
        c += 1
        digits.append(num % 10)
        num /= 10
    print c
    for i in range(c):
        print digits[i]


if __name__ == "__main__":
    func(98100)
