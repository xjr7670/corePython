#!/usr/bin/env python

def switchTime(h, m):
    if h > 0:
        the_minutes = h * 60 + m
    else:
        the_minutes = m

    return the_minutes

t = True
while t:
    h = int(raw_input("Please input the hour: "))
    m = int(raw_input("Please input the minutes: "))
    if h >= 0 and h <= 24 and m >= 0 and m <= 60:
        t = False
        break
    else:
        continue


a = switchTime(h, m)
print a
