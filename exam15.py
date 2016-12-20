#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 利用条件运算符的嵌套来完成此题：
       学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam15.py
@time: 2016/12/20 20:08
"""


def func(score):
    return 'A' if score >= 90 else 'B' if score >= 60 else 'C'


if __name__ == "__main__":
    print func(90)
    print func(60)
    print func(40)
