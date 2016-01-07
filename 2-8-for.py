#!/usb/bin/env python

#l2 = [23, 34, 45, 56, 67]
#s, i = 0, 0
#
#for i in l2:
#    s += i
#else:
#    print s
#
l2 = []
s, i = 0, 0

for i in range(0, 5):
    l2.append(int(raw_input("Please in put num %d " % i)))
    s += l2[i]
else:
    print s
