#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 17:25:08 2017

@author: zhangchi
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = [0 for i in xrange(32)]
        for item in nums:
            for i in range(32):
                if (1<<i)&item > 0:
                    d[i] += 1
        result = 0
        for i in range(32):
            d[i] = d[i] % 3
        if d[31] == 0:
            for i in range(32):
                if d[i] == 1:
                    result = result + (1<<i)
        else:
            for i in range(32):
                if d[i] == 0:
                    result = result + (1<<i)
            result = -result - 1
        return result
    
s = Solution()
print s.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2])