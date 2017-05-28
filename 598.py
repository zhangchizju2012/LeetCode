#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 19:29:37 2017

@author: zhangchi
"""

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        rowMin = m
        colMin = n
        for (a,b) in ops:
            rowMin = min(rowMin,a)
            colMin = min(colMin,b)
        return rowMin * colMin
        
s = Solution()
print s.maxCount(3,3,[[2,2],[3,3],[1,3]])