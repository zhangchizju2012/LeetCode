#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 19:32:18 2018

@author: zhangchi
"""

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        row = len(matrix)
        length =len(matrix[0])
        for i in xrange(1-row, length):
            last = None
            for j in xrange(row):
                if 0 <= i+j < length:
                    if last is None:
                        last = matrix[j][i+j]
                    else:
                        if last != matrix[j][i+j]:
                            return False
        return True
    
s = Solution()
matrix = [[1,2],[2,2]]
print s.isToeplitzMatrix(matrix)