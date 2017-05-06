#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 12:11:24 2017

@author: zhangchi
"""

#==============================================================================
# example:
# nums: [1, 3, 6, 7, 9, 4, 10, 5, 6]
# result: [6, 5, 4, 3, 2, 3, 1, 2, 1]
# result的每i项代表nums从第i个开始往后，含有nums[i]这个元素的Longest Increasing Subsequence
# 我的思路是从后往前推
#==============================================================================

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        length = len(nums)
        result = [1] * length
        for i in xrange(length-2,-1,-1):
            temp = - float('inf')
            for j in xrange(i+1,length):
                if nums[i] < nums[j]:
                    temp = max(temp, result[j])
            if temp > 0:
                result[i] = temp + 1
        return max(result)
s = Solution()
print s.lengthOfLIS([1,3,6,7,9,4,10,5,6])