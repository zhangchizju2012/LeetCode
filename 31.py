#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 23:00:59 2017

@author: zhangchi
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        previous = []
        for i in xrange(len(nums)-1,-1,-1):
            if len(previous) == 0 or nums[i] >= previous[-1]:
                previous.append(nums[i])
            else:
                temp = nums[:i]
                tempValue = nums[i]
                for i in xrange(len(previous)):
                    if previous[i] > tempValue:
                        index = i
                        break
                tempValue, previous[index] = previous[index], tempValue
                return temp + [tempValue] + previous
        return previous
    
s = Solution()
print s.nextPermutation([1,1,5])