#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 21:19:16 2017

@author: zhangchi
"""

def selectionSort(alist):
  
    if len(alist)==1:
        return alist
    else:
        minValue = alist[0]
        count = 0
        index = 0
        for item in alist:
            if item < minValue:
                minValue = item
                index = count
            count = count + 1
            
        alist[0], alist[index] = alist[index], alist[0]
        return [alist[0]] + selectionSort(alist[1:])
    
def selectionSort2(alist):
  
    if len(alist)==1:
        return alist
    else:
        minValue = alist[0]
        index = 0
        for count, item in enumerate(alist):
            if item < minValue:
                minValue = item
                index = count
            
        alist[0], alist[index] = alist[index], alist[0]
        return [alist[0]] + selectionSort2(alist[1:])
        
def selectionSort3(alist):
    if len(alist)==1:
        return alist
    else:
        minValue = alist[0]
        index = 0
        for i in range(len(alist)):
            if alist[i] < minValue:
                minValue = alist[i]
                index = i
        alist[0], alist[index] = alist[index], alist[0]
        return [alist[0]] + selectionSort3(alist[1:])
        
def selectionSort4(alist):
    for j in range(len(alist)):
        minValue = alist[j]
        index = j
        for i in range(j,len(alist)):
            if alist[i] < minValue:
                minValue = alist[i]
                index = i
        alist[j], alist[index] = alist[index], alist[j]
    return alist
    
def selectionSort5(alist, current = 0):
    if current == len(alist):
        return alist
    
    else:
        myMin = current
        for index in range(current,len(alist)): #finding the smallest one
            if alist[index] < alist[myMin]:
                myMin = index
                
        temp = alist[current]                   #swapping
        alist[current] = alist[myMin]
        alist[myMin] = temp
        
        current += 1                            #recording from the begging to where is sorted
        alist = selectionSort5(alist,current)   
    return alist
        
alist = [300, 293, 286, 279, 272, 265, 258, 251, 244, 237, 230, 223, 216, 209, 202, 195, 188, 181, 174, 167, 160, 153, 146, 139, 132, 125, 118, 111, 104, 97, 90, 83, 76, 69, 62, 55, 48, 41, 34, 27, 20, 13, 6, 0]
print(selectionSort5(alist))