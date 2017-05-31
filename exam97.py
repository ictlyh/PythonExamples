#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 读写文件
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam97.py
@time: 2016/12/28 19:41
"""

import os


def func():
    fr = open("exam97.py", "r")
    fw = open("exam97.py.bak", "w")
    a = fr.read()
    fr.close()
    fw.write(a)
    fw.close()
    fr = open("exam97.py.bak", "r")
    a = fr.read()
    fr.close()
    print(a)
    os.remove("exam97.py.bak")


if __name__ == "__main__":
    func()
