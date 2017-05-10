#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 19:59:51 2017

@author: zhangchi
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        if row == 0:
            return False
        rowLength = len(matrix[0])
        if rowLength == 0:
            return False
        length = row * rowLength
        left = 0
        right = length - 1
        if matrix[left/rowLength][left%rowLength] == target or matrix[right/rowLength][right%rowLength] == target:
            return True
        while right - left > 1:
            middle = (left + right)/2
            temp = matrix[middle/rowLength][middle%rowLength]
            if temp == target:
                return True
            elif temp > target:
                right = middle
            else:
                left = middle
        return False

s = Solution()
print s.searchMatrix([[2,3,5,11,16]],12)
#==============================================================================
# class Solution(object):
#     # bullshit
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         temp = [item[0] for item in matrix]
#         left = 0
#         right = len(target) - 1
#         while right - left > 1:
#             middle = (left + right) // 2
#             if temp[middle] == target:
#                 return True
#             elif temp[middle] > target:
#                 right = middle
#             else:
#                 left = middle
#                 
#         temp = matrix[]
#         
#==============================================================================
