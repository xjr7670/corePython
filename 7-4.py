#!/usr/bin/env python
#-*- coding:utf-8 -*-

l1 = [1, 2, 3, 4, 5]
l2 = ['a', 'b', 'c', 'd', 'e']

d = {}

l = len(l1)
for i in range(0, l):
    d[l1[i]] = l2[i]

print d
