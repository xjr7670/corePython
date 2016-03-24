#!/usr/bin/env python

import os

fname1 = raw_input('Please enter file name 1: ')
fname2 = raw_input('Please enter file name 2: ')

fobj1 = open(fname1, 'r')
fobj2 = open(fname2, 'a')

fileOneLines = fobj1.readlines()

fobj2.writelines(fileOneLines)
fobj2.write(os.linesep)

fobj1.close()
fobj2.close()
