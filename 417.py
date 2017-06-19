#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 16:10:42 2017

@author: zhangchi
"""

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(matrix)
        if row == 0:
            return []
        length = len(matrix[0])
        result1 = [[False]*length for _ in xrange(row)]
        result2 = [[False]*length for _ in xrange(row)]
        for i in xrange(row):
            maxValue = -float('inf')
            for j in xrange(length):
                if matrix[i][j] >= maxValue:
                    result1[i][j] = True
                    maxValue = matrix[i][j]
                else:
                    break
        for j in xrange(length):
            maxValue = -float('inf')
            for i in xrange(row):
                if matrix[i][j] >= maxValue:
                    result1[i][j] = True
                    maxValue = matrix[i][j]
                else:
                    break
        label = True
        while label:
            label = False
            for i in xrange(1,row):
                for j in xrange(1,length):
                    if result1[i][j] == False:
                        if (matrix[i][j] >= matrix[i][j-1] and result1[i][j-1] == True) \
                            or (matrix[i][j] >= matrix[i-1][j] and result1[i-1][j] == True) \
                            or (j+1 < length and matrix[i][j] >= matrix[i][j+1] and result1[i][j+1] == True) \
                            or (i+1 < row and matrix[i][j] >= matrix[i+1][j] and result1[i+1][j] == True):
                            result1[i][j] = True
                            label = True
                
        for i in xrange(row):
            maxValue = -float('inf')
            for j in xrange(length-1,-1,-1):
                if matrix[i][j] >= maxValue:
                    result2[i][j] = True
                    maxValue = matrix[i][j]
                else:
                    break
        for j in xrange(length):
            maxValue = -float('inf')
            for i in xrange(row-1,-1,-1):
                if matrix[i][j] >= maxValue:
                    result2[i][j] = True
                    maxValue = matrix[i][j]
                else:
                    break
        label = True
        while label:
            label = False
            for i in xrange(row-2,-1,-1):
                for j in xrange(length-2,-1,-1):
                    if result2[i][j] == False:
                        if (matrix[i][j] >= matrix[i][j+1] and result2[i][j+1] == True) \
                            or (matrix[i][j] >= matrix[i+1][j] and result2[i+1][j] == True) \
                            or (j-1>=0 and matrix[i][j] >= matrix[i][j-1] and result2[i][j-1] == True) \
                            or (i-1>=0 and matrix[i][j] >= matrix[i-1][j] and result2[i-1][j] == True):
                            result2[i][j] = True
                            label = True
        
        result = []
        for i in xrange(row):
            for j in xrange(length):
                if result1[i][j] and result2[i][j]:
                    result.append([i,j])
        return result
        
s = Solution()
print s.pacificAtlantic([[1,2,3],[8,9,4],[7,6,5]])