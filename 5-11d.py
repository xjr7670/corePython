#!/usr/bin/env python

def getZheng(a, b):
    if b % a == 0:
        t = True
    else:
        t = False

    return t

c = int(raw_input("Please input one number: "))
d = int(raw_input("Please input another number: "))
r = getZheng(c, d)
print r
