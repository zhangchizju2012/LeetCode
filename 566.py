#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 09:27:27 2017

@author: zhangchi
"""

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row = len(nums)
        col = len(nums[0])
        if row * col != r * c:
            return nums
        temp = []
        for item in nums:
            temp += item
        result = []
        first = 0
        for i in range(c,r*c+c,c):
            result.append(temp[first:i])
            first = i
        return result
        
s = Solution()
nums = [[1,2],[3,4]]
print s.matrixReshape(nums,2,2)