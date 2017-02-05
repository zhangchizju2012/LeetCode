#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 11:26:50 2016

@author: zhangchi
"""

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        height = len(matrix)
        length = len(matrix[0])
        result = []
        for _ in range(height):
            temp = []
            for _ in range(length):
                temp.append(0)
            result.append(temp)
        for i in range(length):
            if matrix[0][i] == '0':
                result[0][i] = 0
            else:
                result[0][i] = 1
        for i in range(height):
            if matrix[i][0] == '0':
                result[i][0] = 0
            else:
                result[i][0] = 1
        for i in range(1,height):
            for j in range(1,length):
                if matrix[i][j] == '0':
                    result[i][j] =0
                else:
                    result[i][j] = min(result[i][j-1],result[i-1][j],result[i-1][j-1]) + 1
        maxValue = -1
        for i in range(height):
            for j in range(length):
                maxValue = max(maxValue,result[i][j])
        return maxValue * maxValue
        
S = Solution()
matrix = ["11","11"]
print S.maximalSquare(matrix)