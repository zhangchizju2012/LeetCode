#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 20:41:39 2017

@author: zhangchi
"""

class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        temp = []
        while N != 0:
            value = N % 10
            temp.append(value)
            N = N // 10
            
        result = []
        for i in xrange(len(temp)):
            item = temp[i]
            if i == 0 or item <= result[-1]:
                result.append(item)
            else:
                result = [9] * len(result) + [item-1]
                    
        returnValue = 0
        for index, item in enumerate(result):
            returnValue += item * (10 ** index)
        return returnValue
    
s = Solution()
print s.monotoneIncreasingDigits(322)