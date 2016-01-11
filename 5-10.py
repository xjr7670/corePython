#!/usr/bin/env python

def switch(h):
    c = (h - 32) * (float(5) / 9)
    return c

h = switch(75)
print '%.2f' % h 
