#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 23:44:30 2017

@author: zhangchi
"""
import math

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        temp = []
        result = ''
        for i in range(1,n+1):
            temp.append(i)
        k = k - 1
        while n != 0:
            position = k // math.factorial(n-1)
            result += str(temp[position])
            temp.pop(position)
            k = k % math.factorial(n-1)
            n -= 1
        return result

s = Solution()
print s.getPermutation(1,1)