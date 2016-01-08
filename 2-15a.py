#!/usr/bin/env python

a = int(raw_input("input num 1: "))
b = int(raw_input("input num 2: "))
c = int(raw_input("inupt num 3: "))

if a > b:
    t = a
    a = b
    b = t
if a > c:
    t = a
    a = c
    c = t
if b > c:
    t = b
    b = c
    c = t

print a, b, c
