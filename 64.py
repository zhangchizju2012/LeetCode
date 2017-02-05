#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 22:25:59 2016

@author: zhangchi
"""

class Solution(object):
    def helpBuildPath(self,m,n):
        if self.dictionary[m-1][n-1] != -1:
            return self.dictionary[m-1][n-1]
        else:
            if m == 1 and n == 1:
                cost = self.map[0][0]
            elif m == 1:
                cost = self.helpBuildPath(m,n-1) + self.map[m-1][n-1]
            elif n == 1:
                cost = self.helpBuildPath(m-1,n) + self.map[m-1][n-1]
            else:
                cost = min(self.helpBuildPath(m-1,n),self.helpBuildPath(m,n-1)) + self.map[m-1][n-1]
            self.dictionary[m-1][n-1] = cost
            return cost
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.map = grid
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        self.dictionary = [[-1]*n for _ in range(m)]
        return self.helpBuildPath(m,n)