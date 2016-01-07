#!/usr/bin/env python

t = True
while t:
    n = int(raw_input("Please input a number of 1-100: "))
    if n >= 1 and n <= 100:
        print n
        t = False
    else:
        print "Number Error!"
        continue
