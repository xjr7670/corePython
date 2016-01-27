#!/usr/bin/env python

def stringSwitch(s):
    s1 = ''
    for i in s:
        if i.isupper():
            s1 += i.lower()
        elif i.islower():
            s1 += i.upper()
        else:
            s1 += i

    return s1

source_string = raw_input("Please enter your string: ")
s = stringSwitch(source_string)
print s
