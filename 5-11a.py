#!/usr/bin/env python

def getOu():
    l = []
    for i in range(0, 21):
        if i % 2 == 0:
            l.append(i)
        else:
            continue

    return l

a = getOu()
print a
