#!/usr/bin/env python

score = []
s = 0
for i in range(0, 3):
    score.append(int(raw_input("Please input your score %d: " % i)))
    s += score[i]
else:
    l = len(score)

avr = float(s) / l
print avr

