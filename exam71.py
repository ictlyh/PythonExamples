#!/usr/bin/env python
# encoding: utf-8

"""
@desc:
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam71.py
@time: 2016/12/26 20:19
"""

N = 3
# stu
# num : string
# name : string
# score[3]: list
student = []
for i in range(5):
    student.append(['', '', []])


def inputstu(stu):
    for i in range(N):
        stu[i][0] = input('input student num:\n')
        stu[i][1] = input('input student name:\n')
        for j in range(3):
            stu[i][2].append(int(input('score:\n')))


def outputstu(stu):
    for i in range(N):
        print('%-6s%-10s' % (stu[i][0], stu[i][1] ))
        for j in range(3):
            print('%-8d' % stu[i][2][j])

if __name__ == '__main__':
    print()
    # inputstu(student)
    # print(student)
    # outputstu(student)
