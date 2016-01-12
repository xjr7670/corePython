#!/usr/bin/env python
#-*- coding: utf-8 -*-

def getNum(a, b):
    i = a
    while i > 0:
        if a % i == 0 and b % i == 0:
             y = a * b / i
             return [i, y]
             break
        else:
            i -= 1
            continue


a = int(raw_input("Please inupt a: "))
b = int(raw_input("Please input b: "))
if a > b:
    t = a
    a = b
    b = t

s = getNum(a, b)
print "最大公约数是：%d" % s[0]
print "最小公倍数是：%d" % s[1]
