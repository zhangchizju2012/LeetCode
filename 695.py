#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 19:41:09 2017

@author: zhangchi
"""

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        self.dic = {}
        row = len(grid)
        if row == 0:
            return 0
        length = len(grid[0])
        if length == 0:
            return 0
        for i in xrange(row):
            for j in xrange(length):
                self.dic[(i,j)] = grid[i][j]
                
        for i in xrange(row):
            self.dic[(i,-1)] = 0
            self.dic[(i,length)] = 0
        for i in xrange(length):
            self.dic[(-1,i)] = 0
            self.dic[(row,i)] = 0
            
        for i in xrange(row):
            for j in xrange(length):
                #if self.dic[(i,j)] == 1:
                temp = self.helper(i, j)
                result = max(temp, result)
        return result
                    
    def helper(self, a, b):
        if self.dic[(a,b)] == 0:
            return 0
        else:
            count = 1
            self.dic[(a,b)] = 0 # 置为0，避免反复来到这里
            # 分别统计往上下左右的个数
            count += self.helper(a+1,b)
            count += self.helper(a,b+1)
            count += self.helper(a-1,b)
            count += self.helper(a,b-1)
            return count
        
s = Solution()
a = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print s.maxAreaOfIsland([[0]])