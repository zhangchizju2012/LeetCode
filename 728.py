#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 19:34:12 2017

@author: zhangchi
"""

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in xrange(left, right + 1):
            if self.check(i):
                result.append(i)
        return result
    
    def check(self, number):
        temp = number
        while temp > 0:
            if temp % 10 == 0 or number % (temp % 10) != 0:
                return False
            temp = temp // 10
        return True
            
        
s = Solution()
print s.selfDividingNumbers(1,10000)