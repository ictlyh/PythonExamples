#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
       已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他
       不和x,z比，请编程序找出三队赛手的名单。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam22.py
@time: 2016/12/21 19:56
"""


def func():
    bteam = ['x', 'y' , 'z']
    for a in bteam:
        for b in bteam:
            for c in bteam:
                if a != 'x' and c != 'x' and c != 'z' and a != b and b != c and c != a:
                    print('a ->', a)
                    print('b ->', b)
                    print('c ->', c)

if __name__ == "__main__":
    func()
