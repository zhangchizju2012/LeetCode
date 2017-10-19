#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 10:34:54 2017

@author: zhangchi
"""

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        change = sorted(nums)
        length = len(nums)
        if nums == change:
            return 0
        for i in xrange(length):
            if nums[i] != change[i]:
                left = i
                break
        for i in xrange(length-1,-1,-1):
            if nums[i] != change[i]:
                right = i
                break
        return right - left + 1
    
s = Solution()
print s.findUnsortedSubarray([])