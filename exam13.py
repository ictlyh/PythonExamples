#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
       例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam13.py
@time: 2016/12/20 19:50
"""

def isspecial(n):
    c = n
    a = c / 100
    c %= 100
    b = c / 10
    c %= 10
    if a ** 3 + b ** 3 + c ** 3 == n:
        return True
    else:
        return False


if __name__ == "__main__":
    for i in range(100, 1000):
        if isspecial(i):
            print i, 'is a special number'
        # else:
        #    print i, 'is not a special number'

