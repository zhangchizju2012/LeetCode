#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 19:34:51 2017

@author: zhangchi
"""

def divide(m, n):
    if n == 1:
        return [[m]]
    else:
        result = []

        for i in xrange(m//n+1):
            temp = divide(m-i, n-1)
            for item in temp:
                if i <= item[0]:
                    result.append([i] + item)
                    
        return result

def divide_3(m, n):
    if n == 1:
        return [[m]]
    else:
        result = []
        if m % n == 0:
            value = m // n
        else:
            value = m // n + 1
        for i in xrange(0,value):
            temp = divide(m-i, n-1)
            for item in temp:
                result.append(item + [i])
        return result
    

def divide_2(m, n):
    if n == 1:
        return [[m]]
    else:
        result = set()
        for i in xrange(m):
            temp = divide(m-i, n-1)
            for item in temp:
                addItem = tuple(sorted(item + [i]))
                if addItem not in result:
                    result.add(addItem)
        returnResult = []
        for item in result:
            returnResult.append(list(item))
        return returnResult
    
a= divide(30,7)
b= len(divide(30,7))
c= divide_2(30,7)
d= len(divide_2(30,7))
e= a.sort() 
f= c.sort()