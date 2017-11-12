#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 19:31:07 2017

@author: zhangchi
"""

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        total = sum(nums)
        left = 0
        for index, item in enumerate(nums):
            temp = left * 2
            if temp == total - item:
                return index
            else:
                left += item
        return -1
            
s = Solution()
print s.pivotIndex([-1,-1,-1,-1,-1,0])