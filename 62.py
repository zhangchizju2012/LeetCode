#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 22:00:47 2016

@author: zhangchi
"""
#import numpy as np

class Solution(object):
    def helpBuildPath(self,m,n):
        if self.dictionary[m-1][n-1] != 0:
            return self.dictionary[m-1][n-1]
        else:
            if m == 1:
                value = self.helpBuildPath(m,n-1)
            elif n == 1:
                value = self.helpBuildPath(m-1,n)
            else:
                value = self.helpBuildPath(m,n-1) + self.helpBuildPath(m-1,n)
            self.dictionary[m-1][n-1] = value
            return value
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        self.dictionary = [[0]*n for _ in range(m)]  #[[0]*n]*m会有问题
        self.dictionary[0][0] = 1
        return self.helpBuildPath(m,n)

S = Solution()
print S.uniquePaths(3,7)
        