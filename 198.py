#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 15:27:57 2016

@author: zhangchi
"""

class Solution(object):
    def helpRob(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            value = nums[0]
            self.dictionary[0] = value
            return value
        if self.dictionary[len(nums)-1] != -1:
            return self.dictionary[len(nums)-1]
        else:
            value = max(self.helpRob(nums[1:]),self.helpRob(nums[2:])+nums[0])
            self.dictionary[len(nums)-1] = value
            return value
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.dictionary = [-1] * len(nums)
        return self.helpRob(nums)
    