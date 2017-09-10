#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 19:31:24 2017

@author: zhangchi
"""

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <= 1:
            return length
        else:
            result = 1
            count = 0
            previous = -float('inf')
            for item in nums:
                if item > previous:
                    previous = item
                    count += 1
                    result = max(result,count)
                else:
                    previous = item
                    count = 1
            return result
        
s = Solution()
print s.findLengthOfLCIS([2,2,2,2,2])