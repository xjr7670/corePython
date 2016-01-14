#!/usr/bin/env python

nl = []

for i in range(0, 10):
    j = int(raw_input("enter your number: "))
    nl.append(j)
else:
    nl.sort(reverse=True)
    print nl
