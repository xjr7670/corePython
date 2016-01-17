#!/usr/bin/env python
#-*- coding:utf-8 -*-

#s = "abk"
s = raw_input("Please input your string: ")
l = len(s)
t = False
for i in range(0, l):
    # n = i + 2是用于避免单个字符重复也被判断为字符串重复
    n = i + 2
    for j in range(n, l):
        '''取得子字符串并计算其在主字符串中出现的次数，大于1次即表明有重复'''
        s_sub = s[i:j]
	if s.count(s_sub) > 1:
	    t = True
	else:
	    continue
else:
    if t:
        print "Yes"
    else:
        print "No"
