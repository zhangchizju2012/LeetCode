#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 23:32:58 2017

@author: zhangchi
"""

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = []
        for i in xrange(num+1):
            result.append(self.helper(i))
        return result
        
    def helper(self, n):
        count = 0
        temp = 1
        while temp <= n:
            if temp & n > 0:
                count += 1
            temp *= 2
        return count
        
s = Solution()
print s.countBits(5)