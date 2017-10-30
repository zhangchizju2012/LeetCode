#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 19:46:44 2017

@author: zhangchi
"""

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        lengthA = len(A) + 1
        lengthB = len(B) + 1
        result = [[0] * lengthA for _ in xrange(lengthB)]
        for i in xrange(1, lengthB):
            for j in xrange(1, lengthA):
                if A[j-1] == B[i-1]:
                    result[i][j] = result[i-1][j-1] + 1
                else:
                    result[i][j] = 0
        return max([max(item) for item in result])
    
s = Solution()
result = s.findLength([1,2,3,2,1], [3,2,1,4,7])