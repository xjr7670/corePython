#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random

st = raw_input("Please pick up one of this: 'stone/clipper/cloth': ")
r = ['stone', 'clipper', 'cloth']

i = random.randint(1, 3)

if st == r[i]:
    print 'draw'
elif st == 'stone' and r[i] == 'cloth':
    print 'lose'
    elif st == 'stone' and r[i] == ''