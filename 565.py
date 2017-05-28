#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 19:49:22 2017

@author: zhangchi
"""

class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        result = -float('inf')
        for index in range(len(nums)):
            count = 1
            dic[index] = 1
            while True:
                if nums[index] not in dic:
                    count += 1
                    dic[nums[index]] = 1
                    index = nums[index]
                else:
                    result = max(result,count)
                    break
        return result
        
s = Solution()
print s.arrayNesting([1,2,3,4,0])
