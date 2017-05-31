#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 判断101-200之间有多少个素数，并输出所有素数。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam12.py
@time: 2016/12/20 19:42
"""


def isprime(n):
    for i in range(2, int(n / 2)):
        if n % i == 0:
            return False
    return True


def func(a, b):
    cc = 0
    ps = []
    for i in range(a, b):
        if isprime(i):
            cc += 1
            ps.append(i)
    return cc, ps


if __name__ == "__main__":
    c, primes = func(100, 200)
    print('c = ', c)
    for i in primes:
        print(i)
