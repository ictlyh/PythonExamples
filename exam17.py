#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam17.py
@time: 2016/12/21 19:23
"""


def func(s):
    letter = 0
    space = 0
    digit = 0
    others = 0
    for i in s:
        if i.isalpha():
            letter += 1
        elif i.isspace():
            space += 1
        elif i.isdigit():
            digit += 1
        else:
            others += 1
    print('letters = ', letter)
    print('space = ', space)
    print('digit = ', digit)
    print('other = ', others)


if __name__ == "__main__":
    func("hello ni hao 98 $$%! 0")
