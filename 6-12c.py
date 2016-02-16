#!/usr/bin/env python
#-*- coding:utf-8 -*-

def subchr(string, origchar, newchar):
    l1 = len(string)
    l2 = len(origchar)
    t = False
    for i in range(0, l2):
        for j in range(0, l1):
            # 两次循环历遍，只是为了寻找第一个相同的字符
            while origchar[i] == string[j]:
                # 如果发现有相同的字符，则开始逐个比较
                k = j
                i += 1
                j += 1
                if i == l2:
                    # 如果最终比较的长度达到了子字符串的长度
                    # 说明前面的匹配都成功，表示有子字符串包含在内
                    # 把t设为True
                    t = True
                    break
            if t:
                # 如果t是Ture，则后面的不需要再比较了
                break
        if t:
            # 如果t是Ture，则后面的不需要再比较了，跳出最外层for循环
            break

    if t:
        # k减去子字符串的长度，再加1，就是初次发现有相同字符的位置
        kb = k - l2 + 1
        s = string[:kb] + newchar + string[k+1:]
        return s
    else:
        return -1

s1 = raw_input("please enter your string: ")
s2 = raw_input("Please enter which you want to find: ")
s3 = raw_input("Please enter which words you want to replace to: ")
res = subchr(s1, s2, s3)
print res
