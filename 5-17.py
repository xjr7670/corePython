#!/usr/bin/env python
#-*- coding:utf-8 -*-
import random

# 确定列表元素个数1-100
N = random.randint(1, 100)


l = []
# 给列表赋值
for i in range(0, N):
    # 取得随机数用于赋值，列表值范围为0-2**31 -1
    n = random.randint(0, 2**31 -1)
    l.append(n)

# 从已随机生成的列表中随机取出一部分用于排序后显示
l2 = []

# l2的元素个数不能大于l，所以为1-N
N2 = random.randint(1, N)
for j in range(0, N2):
    # 取随机数作为键值，键值不能大于l的长度，也不能大于元素个数，所以为0-N2
    n2 = random.randint(0, N2)
    l2.append(l[n2])
else:
    # 排序之
    l2 = sorted(l2)

print l2

