#!/usr/bin/env python

def getJi():
    l = []
    for i in range(0, 21):
        if i % 2 == 0:
            continue
        else:
            l.append(i)

    return l

b = getJi()
print b
