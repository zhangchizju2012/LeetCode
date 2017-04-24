#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 22:56:33 2017

@author: zhangchi
"""

class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        length = len(n)
        candidate = []
        if length % 2 == 1:
            before = length // 2 + 1
            beforeNumber = int(n[:before])
            temp1 = str(beforeNumber+1)#[-1*before:]
            temp2 = str(beforeNumber)
            temp3 = str(beforeNumber-1)
            candidate.append(int(temp1+temp1[:-1][::-1]))
            candidate.append(int(temp2+temp2[:-1][::-1]))
            candidate.append(int(temp3+temp3[:-1][::-1]))
        else:
            before = length // 2
            beforeNumber = int(n[:before])
            temp1 = str(beforeNumber+1)#[-1*before:]
            temp2 = str(beforeNumber)
            temp3 = str(beforeNumber-1)
            candidate.append(int(temp1+temp1[::-1]))
            candidate.append(int(temp2+temp2[::-1]))
            candidate.append(int(temp3+temp3[::-1]))
        if length > 1:
            candidate.append(int("9"*(length-1)))
        candidate.append(int("1"+"0"*(length-1)+"1"))
        candidate.sort()
        diff = float('inf')
        result = None
        for item in candidate:
            if abs(item - int(n)) < diff and item != int(n):
                result = item
                diff = abs(item - int(n))
        return str(result)