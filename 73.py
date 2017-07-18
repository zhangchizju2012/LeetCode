#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 01:07:59 2017

@author: zhangchi
"""

class Solution(object):
    # Could you devise a constant space solution?
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        dicR = set()
        dicC = set()
        for i in xrange(row):
            for j in xrange(col):
                if matrix[i][j] == 0:
                    dicR.add(i)
                    dicC.add(j)
        for item in dicR:
            for i in xrange(col):
                matrix[item][i] = 0
        for item in dicC:
            for i in xrange(row):
                matrix[i][item] = 0