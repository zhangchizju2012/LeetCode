#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 12:04:27 2017

@author: zhangchi
"""

# much slower, dfs        
class Solution(object):
    def __init__(self):
        self.result = 0
        
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for item in nums:
            if item == target:
                self.result += 1
            elif item < target:
                self.combinationSum4(nums, target - item)
        return self.result        

s = Solution()
print s.combinationSum4([3,4,5,6,7,8,9,10],10)