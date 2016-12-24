#!/usr/bin/env python
# encoding: utf-8

"""
@desc: 学习使用按位取反~。
@author: Yuanhao Luo
@contact: luoyuanhao@software.ict.ac.cn
@file: exam55.py
@time: 2016/12/24 20:45
"""

'''
'b' - 二进制。将数字以2为基数进行输出。
'c' - 字符。在打印之前将整数转换成对应的Unicode字符串。
'd' - 十进制整数。将数字以10为基数进行输出。
'o' - 八进制。将数字以8为基数进行输出。
'x' - 十六进制。将数字以16为基数进行输出，9以上的位数用小写字母。
'e' - 幂符号。用科学计数法打印数字。用'e'表示幂。
'g' - 一般格式。将数值以fixed-point格式输出。当数值特别大的时候，用幂形式打印。
'n' - 数字。当值为整数时和'd'相同，值为浮点数时和'g'相同。不同的是它会根据区域设置插入数字分隔符。
'%' - 百分数。将数值乘以100然后以fixed-point('f')格式打印，值后面会有一个百分号。
'''

def func():
    print '~0X00FF = ', ~0X00FF
    print '~0X0A0B = ', ~0X0A0B
    print '{0:b}'.format(3)
    print '{0:c}'.format(30)
    print '{0:d}'.format(3)
    print '{0:o}'.format(10)
    print '{0:x}'.format(30)
    print '{0:e}'.format(3)
    print '{0:f}'.format(3)
    print '{0:g}'.format(3)
    print '{0:n}'.format(3)
    print '{0:n}'.format(3.1415)
    print '{0:%}'.format(0.15)


if __name__ == "__main__":
    func()
