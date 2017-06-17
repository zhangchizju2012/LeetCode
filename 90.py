#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 21:13:54 2017

@author: zhangchi
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        else:
            nums.sort()
            result = self.helper(nums)
            return [list(item) for item in result]
    
    def helper(self, nums):
        if len(nums) == 1:
            return set([(),(nums[0],)])
        else:
            previous = self.helper(nums[1:])
            temp = set(previous)
            for item in previous:
                temp.add(tuple([nums[0]]+list(item)))
            return temp
            
s = Solution()
print s.subsetsWithDup([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
            
            