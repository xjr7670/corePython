#!/usr/bin/env python

def exchange(dol):
    d = dol * 100
    if d > 25:
        n1 = d / 25
        t1 = d % 25
        if t1 > 10:
            n2 = t1 / 10
            t2 = t1 % 10
        elif  > 5 and n1 < 10:
            