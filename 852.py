#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 18:31:25 2018

@author: zhangchi
"""

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        last = A[0]
        for i in range(1, len(A)):
            if A[i] < last:
                return i - 1
            else:
                last = A[i]
                
s = Solution()
print s.peakIndexInMountainArray([0,2,1,0])