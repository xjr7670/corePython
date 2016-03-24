#!/usr/bin/env python

f = int(raw_input('(f)rom = '))
t = int(raw_input('(t)o = '))
i = int(raw_input('(i)ncrement = '))

for i in range(f, t, i):
    print i
else:
    if (t - f) % i != 0:
        print t