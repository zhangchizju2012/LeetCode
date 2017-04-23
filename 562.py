#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 20:00:52 2017

@author: zhangchi
"""

class Solution(object):
    def count(self,alist):
        count = 0
        result = 0
        for item in alist:
            if item == 1:
                count += 1
                result = max(count,result)
            else:
                count = 0
        return result
        
    def get_rows(self,grid):
        return [[c for c in r] for r in grid]

    def get_cols(self,grid):
        return zip(*grid)
        
    def get_backward_diagonals(self,grid):
        b = [None] * (len(grid) - 1)
        grid = [b[i:] + r + b[:i] for i, r in enumerate(self.get_rows(grid))]
        return [[c for c in r if not c is None] for r in self.get_cols(grid)]

    def get_forward_diagonals(self,grid):
        b = [None] * (len(grid) - 1)
        grid = [b[:i] + r + b[i:] for i, r in enumerate(self.get_rows(grid))]
        return [[c for c in r if not c is None] for r in self.get_cols(grid)]
                
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        row = len(M)
        if row == 0:
            return 0
        col = len(M[0])
        
        result = 0
        for item in M:
            result = max(result,self.count(item))
        
        if row > result:
            tempM = zip(*M)
            for item in tempM:
                result = max(result,self.count(item))
        
        if min(row,col) > result:
            forwardM = self.get_forward_diagonals(M)
            for item in forwardM:
                if len(item) > result:
                    result = max(result,self.count(item))
        
        if min(row,col) > result:
            backwardM = self.get_backward_diagonals(M)
            for item in backwardM:
                if len(item) > result:
                    result = max(result,self.count(item))
                
        return result
        
s = Solution()
a = [[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]]
print s.longestLine(a)
        
            
        