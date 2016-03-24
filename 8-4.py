#!/usr/bin/env python

def isprime(n):
    h = n / 2
    t = False
    while h > 1:
        if n % h == 0:
            break
        h -= 1
    else:
        t = True

    return t

num = int(raw_input('Please input your number: '))
n = isprime(num)
print n
