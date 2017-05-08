#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 22:09:04 2017

@author: zhangchi
"""

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = min(nums)
        result = [item-temp for item in nums]
        return sum(result)