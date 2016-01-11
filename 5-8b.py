#!/usr/bin/env python

P = 3.14
def getTheSum(r, y):
    global P
    if y == "y":
        s = P * r * r
    elif y == "q":
        s = float((4 * P * r * r * r)) / 3

    return s

s1 = getTheSum(3, 'y')
s2 = getTheSum(3, 'q')
print s1
print s2
