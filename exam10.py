#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 暂停一秒输出。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam10.py
@time: 2016/12/19 21:21
"""

import time


if __name__ == "__main__":
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    # 暂停一秒
    time.sleep(1)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
