#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 文本颜色设置。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam35.py
@time: 2016/12/22 21:11
"""


def func():
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
    print bcolors.HEADER, "HEADER"
    print bcolors.OKBLUE, "OKBLUE"
    print bcolors.OKGREEN, "OKGREEN"
    print bcolors.WARNING, "WARNING"
    print bcolors.FAIL, "FAIL"
    print bcolors.ENDC, "ENDC"
    print bcolors.BOLD, "BOLD"
    print bcolors.UNDERLINE, "UNDERLINE"


if __name__ == "__main__":
    func()

