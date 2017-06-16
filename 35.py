#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 17:04:15 2017

@author: zhangchi
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0 or nums[0] >= target:
            return 0
        else:
            for index, item in enumerate(nums):
                if item >= target:
                    return index
            return len(nums)
            
s = Solution()
temp = [5,2,7,0]
for item in temp:
    print s.searchInsert([1,3,5,6],item)
            
            