#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 12:32:12 2016

@author: zhangchi
"""

class Solution(object):
    def getValue(self,temp):
        value = -1
        length = len(temp)
        position = 0#找到0的位置，从0后面的数开始考虑
        for i in range(length):
            if temp[i] == 0:
                position = i
        for i in range(position,length):
            tempValue = min(temp[i:]) * (length - i)
            value = max(value,tempValue)
        return value
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        height = len(matrix)
        length = len(matrix[0])
        result = []
        for i in range(height):
            temp = []
            for j in range(length):
                if matrix[i][j] == '0':
                    temp.append(0)
                else:
                    if len(temp) == 0:
                        temp.append(1)
                    else:
                        temp.append(temp[-1]+1)
            result.append(temp)
            
        for i in range(length):
            temp = []
            for j in range(height):
                temp.append(result[j][i])
                if result[j][i] == 0:
                    pass
                else:
                    result[j][i] = self.getValue(temp)
        
        maxValue = -1
        for i in range(height):
            for j in range(length):
                maxValue = max(maxValue,result[i][j])
        return maxValue
        
        
            
S = Solution()
matrix = ["1011110","1011111","0111111","1011110"]
print S.maximalRectangle(matrix)