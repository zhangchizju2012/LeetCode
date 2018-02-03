#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 16:03:32 2018

@author: zhangchi
"""

def findMaxMin(A):
    length = len(A)
    if length == 1:
        return A[0], A[0]
    if A[0] > A[1]:
        maxValue = A[0]
        minValue = A[1]
    else:
        maxValue = A[1]
        minValue = A[0]
    for i in range(1, length // 2):
        if A[2*i+1] > A[2*i]:
            tempMax = A[2*i+1]
            tempMin = A[2*i]
        else:
            tempMax = A[2*i]
            tempMin = A[2*i+1]
        if tempMax > maxValue:
            maxValue = tempMax
        if tempMin < minValue:
            minValue = tempMin
    if length % 2 == 0:
        return maxValue, minValue
    else:
        if A[length-1] > maxValue:
            maxValue = A[length-1]
        elif A[length-1] < minValue:
            minValue = A[length-1]
        return maxValue, minValue
            
            
A = [2,1,4,5,0]
#A = [2]
#A = [2,1]
print(findMaxMin(A))