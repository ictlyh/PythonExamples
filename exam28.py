#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 有5个人坐在一起，问第五个人多少岁？
       他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。
       问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。
       最后问第一个人，他说是10岁。请问第五个人多大？
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam28.py
@time: 2016/12/22 20:33
"""

def func(i):
    if i == 1:
        return 10
    else:
        return func(i - 1) + 2


if __name__ == "__main__":
    print func(5)
