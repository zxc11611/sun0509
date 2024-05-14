# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:12:40 2024

@author: USER
"""

number = [10,20,30,40,50,60,70,80,90]
print(number[0])
print(number[-1])
print(number[-2])
#切片
print(number[2:6])
print(number[3:])
print(number[:4])
print(number[1:8:2])

print(number[-1::-1])
print(number[-1::-2])

names = ['Bill','Mary']
names.append("John")
names.append("Sue")
print(names)
names.insert(1,'Peter')
print(names)

