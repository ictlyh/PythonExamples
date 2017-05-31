#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 反向输出一个链表。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam73.py
@time: 2016/12/26 20:27
"""


def func(lists):
    print(",".join(str(ele) for ele in lists))
    lists.reverse()
    print(",".join(str(ele) for ele in lists))


if __name__ == "__main__":
    func([1, 2, 3, 4, 5])
    func(['nice', 'to', 'meet', 'you'])

