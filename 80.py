#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 19:37:48 2017

@author: zhangchi
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <= 2:
            return length
        previous = nums[0]
        count = 1
        result = []
        valueList = []
        for i in xrange(1,length):
            if nums[i] == previous:
                count += 1
            else:
                result.append(count)
                valueList.append(previous)
                count = 1
                previous = nums[i]
        result.append(count)
        valueList.append(previous)
        final = 0
        begin = 0
        for item,value in zip(result,valueList):
            gap = min(2,item)
            final += gap
            nums[begin:begin+gap] = [value] * gap
            begin = begin + gap
        return final
        
s = Solution()
print s.removeDuplicates([1,1,1,2,2,3])