#!/usr/bin/env python

fobj = open('8-5.py', 'r')
lines = fobj.readlines()
fobj.close()

for eachLine in lines:
    if eachLine[0] == '#':
        continue
    else:
        print eachLine