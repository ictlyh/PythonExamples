#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 模仿静态变量的用法。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam41.py
@time: 2016/12/23 18:58
"""


def varfunc():
    var = 0
    print('var = %d' % var)
    var += 1
if __name__ == '__main__':
    for i in range(3):
        varfunc()

class Static:
    StaticVar = 5
    def varfunc(self):
        self.StaticVar += 1
        print(self.StaticVar)

print(Static.StaticVar)
a = Static()
for i in range(3):
    a.varfunc()