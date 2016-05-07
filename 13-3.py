#!/usr/bin/env python

def dollarize(f):
    if isinstance(f, float):
        f = str(f)
        l = len(f)
        f1 = f.split('.')
        k = 0
        for i in range(-1, -l):
            k += 1
            if k % 3 == 0:
                f2
