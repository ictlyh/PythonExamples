#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 链表排序
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam74.py
@time: 2016/12/26 20:31
"""


def func(lists):
    print(",".join(str(ele) for ele in lists))
    lists.sort()
    print(",".join(str(ele) for ele in lists))


if __name__ == "__main__":
    func([1, 2, 5, 4, 3])
    func(['nice', 'to', 'meet', 'you'])
