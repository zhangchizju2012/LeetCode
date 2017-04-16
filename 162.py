#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 22:18:18 2017

@author: zhangchi
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        previous = -float('inf')
        nums.append(-float('inf'))
        for i, item in enumerate(nums):
            if item > previous:
                previous = item
            else:
                return i - 1