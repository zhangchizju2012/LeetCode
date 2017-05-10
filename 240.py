#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 22:31:40 2017

@author: zhangchi
"""

class Solution(object):
    # 核心：右上角的数，变小是向左，变大是向下；左下角的数，变大是向右，变小是向上 （抓住这个特性，可以遍历）
    # 对74. 240可以用相同的思路解决
    # inspired by https://www.youtube.com/watch?v=DmP0LNDAR9E
    # binary search & divide and conquer algorithm need to be put forward
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        if row == 0:
            return False
        rowLen = len(matrix[0])
        if rowLen == 0:
            return False
        x = 0
        y = rowLen - 1
        while x < row and y >= 0:
            temp = matrix[x][y]
            if temp == target:
                return True
            elif temp > target:
                y -= 1
            else:
                x += 1
        return False
                