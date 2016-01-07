#!/usr/bin/env python

#l = [3, 4, 323, 75, 77]
#s, i = 0, 0
#le = len(l)
#while i < le:
#    s += l[i]
#    i += 1
#else:
#    print "The sum of the list is: %d" % s

l1 = []
s, i = 0, 0

while i < 5:
    l1.append(int(raw_input("Please input num %d " % i)))
    s += l1[i]
    i += 1
else:
    print s
