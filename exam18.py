#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
       例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam18.py
@time: 2016/12/21 19:28
"""


def func(digit, number):
    s = 0
    exp = ''
    isfirst = True
    for i in range(1, number + 1):
        tmp = str(digit) * i
        s += int(tmp)
        if isfirst:
            exp += tmp
            isfirst = False
        else:
            exp += ' + ' + tmp
    print(exp, ' = ', s)


if __name__ == "__main__":
    func(2, 5)
