#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 19:47:47 2017

@author: zhangchi
"""

class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dic = {}
        result = 0
        row = len(grid)
        length = len(grid[0])
        for i in xrange(row):
            temp = []
            for j in xrange(length):
                if grid[i][j] == 1:
                    temp.append(j)
            tempLength = len(temp)
            for m in xrange(tempLength):
                for n in xrange(m+1,tempLength):
                    value = temp[m] + temp[n] * 1000
                    if value in dic:
                        result += dic[value]
                        dic[value] += 1
                    else:
                        dic[value] = 1
        return result
    
grid = [[1, 0, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [0, 0, 0, 1, 0],
 [1, 0, 1, 0, 1]]
s = Solution()
print s.countCornerRectangles(grid)