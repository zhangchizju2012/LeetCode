#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 11:59:22 2016

@author: zhangchi
"""

class Solution(object):
    def helpBuildPath(self,m,n):
        if self.dictionary[m-1][n-1] is not None:
            return self.dictionary[m-1][n-1]
        else:
            if m == 1 and n == 1:
                value = self.map[0][0]
            elif n == 1:
                value = self.helpBuildPath(m-1,n) + self.map[m-1][n-1]
            elif n == m:
                value = self.helpBuildPath(m-1,n-1) + self.map[m-1][n-1]
            else:
                value = min(self.helpBuildPath(m-1,n-1),self.helpBuildPath(m-1,n)) + self.map[m-1][n-1]
            self.dictionary[m-1][n-1] = value
            return value
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.map = triangle
        m = len(triangle)
        self.dictionary = [[None]*m for _ in range(m)]
        minValue = float('inf')
        for i in range(m):
            temp = self.helpBuildPath(m,i+1)
            if temp < minValue:
                minValue = temp
        return minValue
        
S = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print S.minimumTotal(triangle)