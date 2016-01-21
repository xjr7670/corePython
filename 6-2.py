#!/usr/bin/env python

import string
import keyword

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v2.0'
print 'Testees must be at least 1 chars long.!'
myInput = raw_input('Identifier to test?')

if len(myInput) > 0:

    if myInput in keyword.kwlist:
        print "You enter an Python keyword, it could not be a identifier"
    elif myInput[0] not in alphas:
        print '''invalid: first symbol must be alphabetic'''
    else:
        for otherChar in myInput[0:]:
            if otherChar not in alphas + nums:
                print '''invalid: remaining symbols must be alphanumeric'''
                break
        else:
            print "okay as an identifier"
