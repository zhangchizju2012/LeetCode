#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 19:43:42 2018

@author: zhangchi
"""

class Solution(object):
    # 想象成那种阶梯的
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
# =============================================================================
#         maxValue = arr[0]
#         count = 0
#         for i in xrange(len(arr)):
#             if arr[i] > maxValue:
#                 maxValue = arr[i]
#             if i == maxValue:
#                 count += 1
#         return count
#     
# =============================================================================
        maxValue = arr[0]
        count = 0
        for i in xrange(len(arr)):
            if arr[i] > maxValue:
                maxValue = arr[i]
            arr[i] = maxValue
        for i in xrange(len(arr)):
            if i == arr[i]:
                count += 1
        return count
        
# =============================================================================
#         count = 1
#         value = arr[0]
#         left = arr[0]
#         point = 0
#         while left > 0:
#             if arr[point] < value:
#                 point += 
# =============================================================================
# =============================================================================
#         count = 1
#         right = arr[0] + 1
#         while right <= len(arr):
#             if right < arr[right]:
#                 count += 1
#                 right = arr[right]
#         return count
# =============================================================================
    
s = Solution()
print s.maxChunksToSorted([1,2,0,3])