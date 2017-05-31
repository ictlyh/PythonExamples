#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc:
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam98.py
@time: 2016/12/28 19:47
"""

import os


def func():
    fr = open("exam98.py", "r")
    fw = open("exam98.py.bak", "w")
    a = fr.read()
    fr.close()
    fw.write(a.upper())
    fw.close()
    fr = open("exam98.py.bak", "r")
    a = fr.read()
    fr.close()
    print(a)
    os.remove("exam98.py.bak")


if __name__ == "__main__":
    func()