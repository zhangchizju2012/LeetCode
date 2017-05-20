#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 06:19:21 2017

@author: zhangchi
"""

class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return []
        # not sort, nums.sort()
        self.nums = nums
        length = len(nums)
        self.length = length
        result = {}
        for i in xrange(2 ** length):
            tempList = self.helper(i)
            if len(tempList) >= 2:
                if tempList not in result:
                    result[tempList] = 1
        final = []
        for item in result:
            final.append(list(item))
        return final
            
    def helper(self,value):
        temp = []
        for i in xrange(self.length):
            if value & (2**i) > 0:
                if len(temp) == 0 or self.nums[i] >= temp[-1]:
                    temp.append(self.nums[i])
        return tuple(temp)
        
s = Solution()
print s.findSubsequences([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])