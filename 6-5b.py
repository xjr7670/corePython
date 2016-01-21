#!/usr/bin/env python

s1 = raw_input("Please input a string 1: ")
s2 = raw_input("Please input a string 2: ")

l1 = len(s1)
l2 = len(s2)

t = True
if l1 != l2:
    print "l1 != l2"
else:
    for i in range(0, l1):
        if s1[i] == s2[i]:
	    continue
	else:
	    t = False
    else:
        if t:
	    print "l1 == l2"
	else:
	    print "l1 != l2"

