#!/usr/bin/env python

n = int(raw_input("Please choose one to input(1)(2)(X): "))

while n != "X":
	if n == 1:
		l1 = []
		s = 0
		print "Please in five number:"
		for i in range(0, 5):
			l1.append(int(raw_input("num %d" % (i+1))))
			s += l1[i]
		else:
			print "The sum of this five number is: %d" % s
			break
	elif n == 2:
		l2 = []
		s = 0
		print "Please input five number: "
		for i in range(0, 5):
			l2.append(int(raw_input("num %d" % (i+1))))
			s += l2[i]
		else:
			avr = float(s) / 5
			print "The avrage of this five number is: %f" % avr
			break
	else:
    	n = int(raw_input("Please choose one to input(1)(2)(X): "))
