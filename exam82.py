#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 八进制转换为十进制
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam82.py
@time: 2016/12/27 19:36
"""

'''
ord(c):
    Given a string of length one, return an integer representing the Unicode code point
    of the character when the argument is a unicode object, or the value of the byte when
    the argument is an 8-bit string.
    This is the inverse of chr() for 8-bit strings and of unichr() for unicode objects.
'''


def func(odigits):
    n = 0
    for o in odigits:
        n = n * 8 + ord(o) - ord('0')
    return n


if __name__ == "__main__":
    print(func('16'))
