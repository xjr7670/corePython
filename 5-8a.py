#!/usr/bin/env python

def getTangleSquare(line, ln):
    if ln == 4:
        s = line ** 2
    elif ln == 12:
        s = line ** 3
    
    return s

# zhengfangxing
s1 = getTangleSquare(5, 4)
s2 = getTangleSquare(5, 12)

print s1
print s2
