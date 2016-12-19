#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 企业发放的奖金根据利润提成。
       利润(I)低于或等于10万元时，奖金可提10%；
       利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；
       20万到40万之间时，高于20万元的部分，可提成5%；
       40万到60万之间时高于40万元的部分，可提成3%；
       60万到100万之间时，高于60万元的部分，可提成1.5%；
       高于100万元时，超过100万元的部分按1%提成
       从键盘输入当月利润I，求应发放奖金总数？
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam2.py
@time: 2016/12/18 20:21
"""


def func():
    while True:
        # revenue = long(raw_input("Please input your revenue,(0 to exit):"))
        revenue = 100
        if revenue == 0:
            return
        elif revenue < 0:
            print 'invalid revenue', revenue, 'can not be negative'
        else:
            if revenue <= 10:
                award = revenue * 0.1
            elif revenue <= 20:
                award = 10 * 0.1 + (revenue - 10) * 0.075
            elif revenue <= 40:
                award = 10 * 0.1 + 10 * 0.075 + (revenue - 20) * 0.05
            elif revenue <= 60:
                award = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + (revenue - 40) * 0.03
            elif revenue <= 100:
                award = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + (revenue - 60) * 0.015
            else:
                award = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40 * 0.015 + (revenue - 100) * 0.001
            print 'award = ', award
        break


if __name__ == "__main__":
    func()
