#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 13:38:09 2017

@author: zhangchi
"""

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]
        value = 0
        while value < n:
            up = 2 ** value
            length = len(result)
            for i in xrange(length-1,-1,-1):
                result.append(result[i]+up)
            value += 1
        return result
        
s = Solution()
print s.grayCode(1)
            