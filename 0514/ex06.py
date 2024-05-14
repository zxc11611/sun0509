# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:57:19 2024

@author: USER
"""
#count 計次
words = ['a','b','c','d','a','c','f','a','c','c']
a = words.count('a')
f = words.count('f')
g = words.count('g')
print('a有:',a)
print('f有:',f)
print('g有:',g)
# index 找尋目標所在物index
ind = words.index('d')
print('d的索引位置:',ind)
#ind = words.index('z')
#print(ind)
ind = words.index('c')
print(ind)
start = 0
for i in range(words.count('c')):
    ind  = words.index('c',start)
    print('c的索引:',ind)
    start = ind+1#+1是跳過第一的找到的值+1
    