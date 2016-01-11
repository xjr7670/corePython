#!/usr/bin/env python

def calc(ex):
    s = ex.split()
    n1 = int(s[0])
    n2 = s[1]
    n3 = int(s[2])
    if n2 == "+":
        s = n1 + n3
    elif n2 == "-":
        s = n1 - n3
    elif n2 == "*":
        s = n1 * n3
    elif n2 == "/":
        s = float(n1) / n3
    elif n2 == "%":
        s = n1 % n3
    elif n2 == "**":
        s = n1 ** n3

    return s

z = True
while z:
    ex = raw_input("Please input your express: ")
    if len(ex) >= 3 and ex[2] in ['+', '-', '*', '/', '%', '**']:
        z = False
    else:
        continue

s = calc(ex)
print s
