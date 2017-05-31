#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 画椭圆ellipse
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam63.py
@time: 2016/12/25 19:02
"""


from tkinter import *


def func():
    x = 360
    y = 160
    top = y - 30
    bottom = y - 30
    canvas = Canvas(width=400, height=600, bg='white')
    for i in range(20):
        canvas.create_oval(250 - top, 250 - bottom, 250 + top, 250 + bottom)
        top -= 5
        bottom += 5
    canvas.pack()
    #mainloop()


if __name__ == "__main__":
    func()
