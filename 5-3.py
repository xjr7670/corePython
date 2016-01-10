#!/usr/bin/env python

def score(grade):
    if grade >= 90 and grade <= 100:
        s = "A"
    elif grade >= 80 and grade <= 89:
        s = "B"
    elif grade >= 70 and grade <= 79:
        s = "C"
    elif grade >= 60 and grade <= 69:
        s = "D"
    else:
        s = "E"

    return s

myScore = score(0)
print myScore