#!/usr/bin/env python
#-*- coding:utf8 -*-

# get an input
num_str = raw_input('Enter a number: ')

# trun it to integer
num_num = int(num_str)

# get an list variable --> fac_list. and print it
fac_list = range(1, num_num+1)
print "BEFORE:", fac_list

# set a beginer variable i to 0
i = 0

l2 = ''
# delete the .... 
while i < len(fac_list):

    # 余数为0则去除
    if num_num % fac_list[i] == 0:
        # 如果直接在这里删除元素，那么整个字符串的索引就会变了，会出错
        print fac_list[i]
    else:
        l2 += str(fac_list[i])

    # next circlestance
    i = i + 1

# after finish, print it
print "AFTER: ", l2
