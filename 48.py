#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 15:16:41 2016

@author: zhangchi
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length/2):
            for j in range(length/2 + length%2):
                matrix[i][j],matrix[j][length-i-1],matrix[length-i-1][length-j-1],matrix[length-j-1][i] = matrix[length-j-1][i],matrix[i][j],matrix[j][length-i-1],matrix[length-i-1][length-j-1]
        return matrix
#a = [[1]]
#a = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
a = [[1,2],[3,4]]
#a = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
S = Solution()
print S.rotate(a)