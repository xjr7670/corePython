#!/usr/bin/env python

def getBalance(total, mp):
    print "          Amount    Remaining"
    print "  Pymt#  Paid      Balance"
    print "-------  -----    --------"
    m = 0
    ba = total
    p = 0 
    while ba > 0:
        print "%d        $%.2f       $%.2f" % (m, p, ba)
        p = mp
        if ba < p:
            p = ba
            ba = 0
            print "%d        $%.2f       $%.2f" % (m, p, ba)
        ba = ba - p

        m += 1

total = float(raw_input("Enter opening balance: "))
mp = float(raw_input("Enter monthly payment: "))
r = getBalance(total, mp)
