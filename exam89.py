#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下:
    每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam89.py
@time: 2016/12/28 19:09
"""


def func(num):
    a = num / 1000
    num %= 1000
    b = num / 100
    num %= 100
    c = num / 10
    num %= 10
    d = num
    a = (a + 5) % 10
    b = (b + 5) % 10
    c = (c + 5) % 10
    d = (d + 5) % 10
    print(1000 * d + 100 * c + 10 * b + a)


if __name__ == "__main__":
    func(89)
