#!/usr/bin/env python

def stripSpace(s):
    l = len(s)
    for i in range(0, l):
        if s[i] == " ":
            s = s.replace(s[i], "")
        else:
            break

    l1 = len(s)
    for j in range(-l1, -1):
        if s[j] == " ":
            s = s.replace(s1[i], "")
        else:
            break

    return s

s = raw_input("please input your string: ")
ss = stripSpace(s)
print ss
