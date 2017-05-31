#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@desc: 画图，学用line画直线。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam57.py
@time: 2016/12/25 18:35
"""


from tkinter import *


def func():
    canvas = Canvas(width=300, height=300, bg='green')
    canvas.pack(expand=YES, fill=BOTH)
    x0 = 263
    y0 = 263
    y1 = 275
    x1 = 275
    for i in range(19):
        canvas.create_line(x0, y0, x0, y1, width=1, fill='red')
        x0 = x0 - 5
        y0 = y0 - 5
        x1 = x1 + 5
        y1 = y1 + 5
    x0 = 263
    y1 = 275
    y0 = 263
    for i in range(21):
        canvas.create_line(x0, y0, x0, y1, fill='red')
        x0 += 5
        y0 += 5
        y1 += 5
    #mainloop()


if __name__ == "__main__":
    func()

