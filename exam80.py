#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 海滩上有一堆桃子，五只猴子来分。
       第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。
       第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，
       第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam80.py
@time: 2016/12/27 19:17
"""


'''
假设第n只猴子拿走后还剩下f(n) 个桃子，则有：
f(n - 1) = (f(n) / 4) * 5 + 1
其中f(n) 都为整数
'''
def func():
    i = 0
    # 第 n 只猴子拿走了 j 个
    j = 1
    # x 第 n 只猴子拿走后剩下 x 个
    x = 0
    while i < 5:
        # 第 n 只猴子拿走了 j 个，因此还剩下 4 * j 个
        x = 4 * j
        for i in range(0, 5):
            if x % 4 != 0:
                break
            else:
                i += 1
            x = (x / 4) * 5 + 1
        j += 1
    print(x)


if __name__ == "__main__":
    func()
