#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 12:32:57 2017

@author: zhangchi
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        lengthA = len(a)
        lengthB = len(b)
        if lengthA < lengthB:
            a = "0" * (lengthB - lengthA) + a
        else:
            b = "0" * (lengthA - lengthB) + b
        a = a[::-1]
        b = b[::-1]
        temp = 0
        result = ""
        for i in xrange(max(lengthA,lengthB)):
            sumValue = int(a[i]) + int(b[i]) + temp
            if sumValue >= 2:
                result += str(sumValue-2)
                temp = 1
            else:
                result += str(sumValue)
                temp = 0
        if temp == 1:
            result += "1"
        return result[::-1]

s = Solution()
print s.addBinary("11","1")                