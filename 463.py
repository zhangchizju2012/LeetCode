#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 18:40:42 2017

@author: zhangchi
"""

class Solution(object):
    # dfs
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.result = 0
        self.grid = grid
        self.row = len(grid)
        self.length = len(grid[0])
        label = False
        for i in xrange(self.row):
            for j in xrange(self.length):
                if self.grid[i][j] == 1:
                    start = [i,j]
                    self.grid[i][j] = 2 # 踩过的变成2
                    label = True
                    break
            if label is True:
                break
        self.helper(start[0],start[1])
        return self.result
        
        
    def helper(self, i, j):
        if 0 <= i < self.row and 0 <= j + 1 < self.length:
            if self.grid[i][j+1] == 1:
                self.grid[i][j+1] = 2
                self.helper(i, j+1)
            elif self.grid[i][j+1] == 0: # 要是2就忽略，说明是踩过的，0的话说明是边缘
                self.result += 1
        else:
            self.result += 1
            
        if 0 <= i < self.row and 0 <= j - 1 < self.length:
            if self.grid[i][j-1] == 1:
                self.grid[i][j-1] = 2
                self.helper(i, j-1)
            elif self.grid[i][j-1] == 0:
                self.result += 1
        else:
            self.result += 1
            
        if 0 <= i - 1 < self.row and 0 <= j < self.length:
            if self.grid[i-1][j] == 1:
                self.grid[i-1][j] = 2
                self.helper(i-1, j)
            elif self.grid[i-1][j] == 0:
                self.result += 1
        else:
            self.result += 1
            
        if 0 <= i + 1 < self.row and 0 <= j < self.length:
            if self.grid[i+1][j] == 1:
                self.grid[i+1][j] = 2
                self.helper(i+1, j)
            elif self.grid[i+1][j] == 0:
                self.result += 1
        else:
            self.result += 1
        
s = Solution()
a = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
print s.islandPerimeter(a)
            