#!/usr/bin/env python

l1 = ['zone', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

n = int(raw_input("Please input your number: "))

if n < 10:
    n1 = l1[n]
    print n1
elif n > 10 and n < 100:
    n1 = n / 10
    n2 = n % 10
    print l1[n1] + '-' + l1[n2]
else:
    pass
