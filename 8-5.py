#!/usr/bin/env python

def getfactors(n):
    list1 = []
    for i in range(1, n+1):
        if n % i == 0:
            list1.append(i)
        else:
            continue

    return list1


num = int(raw_input('Please enter your number: '))
n = getfactors(num)
print n
