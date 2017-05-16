#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 17:10:20 2017

@author: zhangchi
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 0:
            return x
        count = 0
        while True:
            if (2 ** count) ** 2 > x:
                break
            count += 1
        previous = 2 ** (count-1)
        for item in xrange(2**(count-1),2**count+1):
            if item ** 2 > x:
                return previous
            previous = item
            
s = Solution()
print s.mySqrt(16)