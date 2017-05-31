#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 利用ellipse 和 rectangle 画图
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam64.py
@time: 2016/12/25 19:03
"""


from tkinter import *


def func():
    canvas = Canvas(width=400, height=600, bg='white')
    left = 20
    right = 50
    top = 50
    num = 15
    for i in range(num):
        canvas.create_oval(250 - right, 250 - left, 250 + right, 250 + left)
        canvas.create_oval(250 - 20, 250 - top, 250 + 20, 250 + top)
        canvas.create_rectangle(20 - 2 * i, 20 - 2 * i, 10 * (i + 2), 10 * (i + 2))
        right += 5
        left += 5
        top += 10

    canvas.pack()
    #mainloop()


if __name__ == "__main__":
    func()
