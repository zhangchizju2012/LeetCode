#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 19:28:00 2017

@author: zhangchi
"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        result = sum(nums[:k])
        now = result
        for i in xrange(k,len(nums)):
            now = now + nums[i] - nums[i-k]
            result = max(result, now)
        return result*1.0/k
        
s = Solution()
print s.findMaxAverage([12,-5,-6,50,5],3)