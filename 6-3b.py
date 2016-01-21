#!/usr/bin/env python

nl = []
for i in range(0, 10):
    n = raw_input("Enter your number: ")
    nl.append(n)
else:
    nl.sort()
    print nl
