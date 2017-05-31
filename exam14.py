#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam14.py
@time: 2016/12/20 19:59
"""


def primefacts(n):
    s = str(n) + ' = '
    isfirst = True
    for i in range(2, n + 1):
        while n != 1:
            if n % i == 0:
                if isfirst:
                    s += str(i)
                    isfirst = False
                else:
                    s += ' * ' + str(i)
                n /= i
            else:
                break
    print(s)


if __name__ == "__main__":
    primefacts(90)
