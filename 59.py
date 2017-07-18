#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 21:59:56 2017

@author: zhangchi
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.result = [[0]*n for _ in xrange(n)]
        start = 1
        index = 0
        while start < n ** 2:
            start = self.helper(index,n-1-index*2,start)
            index += 1
        if start == n ** 2:
            self.result[n//2][n//2] = start
        return self.result
                           
    def helper(self, index, length, start):
        for i in xrange(index,index+length):
            self.result[index][i] = start
            start += 1
        for i in xrange(index,index+length):
            self.result[i][index+length] = start
            start += 1
        for i in xrange(index+length,index,-1):
            self.result[index+length][i] = start
            start += 1
        for i in xrange(index+length,index,-1):
            self.result[i][index] = start
            start += 1
        return start
        
s = Solution()
print s.generateMatrix(0)