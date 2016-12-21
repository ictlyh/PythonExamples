#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个
       第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩
       下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam21.py
@time: 2016/12/21 19:48
"""

'''
假设第n天吃完剩下 f(n) 个，则有 2 * (f(n + 1) + 1) = f(n)，已知f(9) = 1，求 f(0)
'''


def func():
    s = 1
    for i in range(9, 0, -1):
        s = (s + 1) * 2
    return s


if __name__ == "__main__":
    print func()
