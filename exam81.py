#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 809*??=800*??+9*??+1 其中??代表的两位数,8*??的结果为两位数，9*??的结果为3位数。
       求??代表的两位数，及809*??后的结果。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam81.py
@time: 2016/12/27 19:32
"""


def func():
    a = 809
    for i in range(10, 100):
        b = i * a + 1
        if (b >= 1000 and b <= 10000) and 8 * i < 100 and 9 * i >= 100:
            print b, '/', i, ' = 809 * ', i, ' + ', b % i


if __name__ == "__main__":
    func()
