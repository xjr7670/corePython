#!/usr/bin/env python

def timeTransition(t):
    if t < 60:
        return t
    elif t > 60:
        h = t / 60
        m = t % 60
        return (h, m)
    else:
        return (01, 00)

getTime = int(raw_input("Please enter your minutes: "))
theTime = timeTransition(getTime)
if isinstance(theTime, tuple):
    print str(theTime[0]) + ':' + str(theTime[1])
else:
    print str(theTime) + ' minutes'
