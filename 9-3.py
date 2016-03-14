#!/usr/bin/env python
'''练习9－3
先读取文件，再读取所有行
然后判断行数'''

fname = raw_input('Please input filename: ')
fobj = open(fname, 'r')

totalLineNum = len(fobj.readlines())
print totalLineNum