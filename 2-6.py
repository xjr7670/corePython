#!/usr/bin/env python

n = raw_input("Please input a number: ")
n = int(n)
if n > 0:
    print str(n) + " is a positive"
elif n < 0:
    print str(n) + " is a negative"
else:
    print "you input 0"
