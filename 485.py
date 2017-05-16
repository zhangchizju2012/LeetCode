#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 23:46:51 2017

@author: zhangchi
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        result = []
        for item in nums:
            if item == 0:
                if count != 0:
                    result.append(count)
                    count = 0
            else:
                count += 1
        result.append(count)
        return max(result)