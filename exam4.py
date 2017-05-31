#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 输入某年某月某日，判断这一天是这一年的第几天？
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam4.py
@time: 2016/12/18 20:50
"""

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isspecialyear(year):
    if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
        return True
    else:
        return False


def func():
    # year = int(raw_input("Year:"))
    # month = int(raw_input("month:"))
    # day = int(raw_input("day:"))
    year = 2015
    month = 6
    day = 7
    count = 0
    for i in range(0, month - 1):
        count += days[i]
    count += day
    if month > 2 and isspecialyear(year):
        count += 1
    print('day count: ', count)


if __name__ == "__main__":
    func()
