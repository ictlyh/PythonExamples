#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam31.py
@time: 2016/12/22 20:55
"""


def func(s):
    if s[0] == 'F':
        return 'Friday'
    elif s[0] == 'M':
        return 'Monday'
    elif s[0] == 'W':
        return 'Wednesday'
    elif s[0] == 'S':
        if s[1] == 'A':
            return 'Saturday'
        elif s[1] == 'u':
            return 'Sunday'
        else:
            return 'Invalid'
    elif s[0] == 'T':
        if s[1] == 'U':
            return 'Tuesday'
        elif s[1] == 'H':
            return 'Thursday'
        else:
            return 'Invalid'
    else:
        return 'Invalid'


if __name__ == "__main__":
    print func('SA')
    print func('TU')
    print func('F')
