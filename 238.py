#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 16:23:53 2017

@author: zhangchi
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1] * len(nums)
        temp = 1
        for i in range(len(nums)):
            result[i] = temp
            temp *= nums[i]
        temp = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= temp
            temp *= nums[i]
        return result
            