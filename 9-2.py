#!/usr/bin/env python

fname = raw_input('Please input your filename: ')
lineNum = raw_input('How many lines you want to show: ')
lineNum = int(lineNum)

fobj = open(fname, 'r')

for i in range(0, lineNum):
    print fobj.readline()

fobj.close()