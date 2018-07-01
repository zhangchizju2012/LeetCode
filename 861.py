#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 19:14:35 2018

@author: zhangchi
"""

# 第一位比后面所有位总和都重要，每行每列只有两种可能，翻和不翻，每行翻不翻可以取决于第一位

class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        result = []
        for item in A:
            if item[0] == 1:
                result.append(item)
            else:
                temp = []
                for i in item:
                    if i == 0:
                        temp.append(1)
                    else:
                        temp.append(0)
                result.append(temp)
        row = len(result)
        length = len(result[0])
        value = 0
        for i in range(length):
            count = 0
            for j in range(row):
                if result[j][i] == 1:
                    count += 1
            if count >= row / 2.:
                value += count * 2 ** (length - i - 1)
            else:
                value += (row-count) * 2 ** (length - i - 1)
        return value
    
s = Solution()
print s.matrixScore( [[0,0,1,1],[1,0,1,0],[1,1,0,0]])