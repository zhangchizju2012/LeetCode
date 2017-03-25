#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 18:20:24 2017

@author: zhangchi
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        length = len(nums)
        for i in range(1<<length):
            temp = []
            for j in range(length):
                if (1<<j)&i > 0:
                    temp.append(nums[j])
            result.append(temp)
        return result
    
s = Solution()
print s.subsets([1,5,8,9])