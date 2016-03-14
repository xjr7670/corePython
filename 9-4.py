#!/usr/bin/env python
'''练习9－4，当前只能实现按回车键继续'''


fname = raw_input('Please input a filename: ')
fobj = open(fname, 'r')
flines = fobj.readlines()

line = 1
for i in flines:
    print i
    line += 1
    if line % 3 == 0:
        raw_input()
