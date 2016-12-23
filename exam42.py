#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 学习使用auto定义变量的用法。没有auto关键字，使用变量作用域来举例吧。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam42.py
@time: 2016/12/23 19:00
"""


num = 2
def autofunc():
    num = 1
    print 'internal block num = %d' % num
    num += 1

if __name__ == "__main__":
    for i in range(3):
        print 'The num = %d' % num
        num += 1
    autofunc()