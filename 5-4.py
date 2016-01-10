#!/usr/bin/env python

def leapYear(year):
    if year % 4 == 0 and year % 100 != 0:
        answer = "Yes"
    elif year % 4 == 0 and year % 100 == 0:
        answer = "Yes"
    else:
        answer = "No"

    return answer

y = leapYear(2400)
print y