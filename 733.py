#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 19:35:48 2017

@author: zhangchi
"""

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.image = image
        self.row  = len(image)
        self.length = len(image[0])
        self.helper(sr, sc, -1)
        for i in xrange(self.row):
            for j in xrange(self.length):
                if self.image[i][j] == -1:
                    self.image[i][j] = newColor
        return self.image
                
    def helper(self, sr, sc, newColor):
        origin = self.image[sr][sc]
        self.image[sr][sc] = newColor
        
        if 0 <= sr - 1 < self.row and 0 <= sc < self.length and self.image[sr-1][sc] == origin:
            self.helper(sr-1, sc, newColor)
        if 0 <= sr + 1 < self.row and 0 <= sc < self.length and self.image[sr+1][sc] == origin:
            self.helper(sr+1, sc, newColor)
            
        if 0 <= sr < self.row and 0 <= sc - 1 < self.length and self.image[sr][sc-1] == origin:
            self.helper(sr, sc-1, newColor)
        if 0 <= sr < self.row and 0 <= sc + 1 < self.length and self.image[sr][sc+1] == origin:
            self.helper(sr, sc+1, newColor)
            
s = Solution()
# =============================================================================
# image = [[0,0,0],[0,1,1]]
# sr = 1
# sc = 1
# newColor = 1
# =============================================================================
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
print s.floodFill(image, sr, sc, newColor)
        
            
        
                    