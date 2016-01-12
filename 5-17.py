#!/usr/bin/env python

import random

def getItem():
    l1 = []
    l2 = []
    N1 = random.randint(1, 100)
    n = random.randint(1, 2**31-1)
    for i in range(0, N1):
        l1.append(n)

    N2 = random.randint(1, 100)
    for j in range(0, N2):
        k = random.randint(0, N1)
        l2.append(l1[k])

    l3 = l2.sort()

    return l3

s = getItem()
print s
