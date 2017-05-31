#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam23.py
@time: 2016/12/21 20:02
"""


from sys import stdout


def func():
    for i in range(4):
        for j in range(2 - i + 1):
            stdout.write(' ')
        for k in range(2 * i + 1):
            stdout.write('*')
        print()
    for i in range(3):
        for j in range(i + 1):
            stdout.write(' ')
        for k in range(4 - 2 * i + 1):
            stdout.write('*')
        print()


if __name__ == "__main__":
    func()
