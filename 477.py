#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 22:19:56 2017

@author: zhangchi
"""

class Solution(object):
    def totalHammingDistance3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = [0 for i in range(32)]
        length = len(nums)
        for i in range(32):
            waitRemove = []
            for item in nums:
                temp = (1<<i)
                if temp > item:
                    waitRemove.append(item)
                else:
                    if temp & item > 0:
                        result[i] += 1
            for item in waitRemove:
                nums.remove(item)#remove takes too much time
        finalResult = 0
        for i in range(32):
            finalResult += result[i] * (length - result[i])
        return finalResult
    
    def totalHammingDistance(self, nums):
        # fastest, easiest
        """
        :type nums: List[int]
        :rtype: int
        """
        result = [0 for i in range(32)]
        length = len(nums)
        for i in range(32):
            for item in nums:
                temp = (1<<i)
                if temp & item > 0:
                    result[i] += 1
        finalResult = 0
        for i in range(32):
            finalResult += result[i] * (length - result[i])
        return finalResult
    
    def totalHammingDistance2(self, nums):
        # better than 3
        """
        :type nums: List[int]
        :rtype: int
        """
        result = [0 for i in range(32)]
        length = len(nums)
        for i in range(32):
            numsNew = []
            for item in nums:
                temp = (1<<i)
                if temp <= item:
                    if temp & item > 0:
                        result[i] += 1
                    numsNew.append(item)
            nums = numsNew
            if len(nums) == 0:
                break
        finalResult = 0
        for i in range(32):
            finalResult += result[i] * (length - result[i])
        return finalResult
    
s = Solution()
print s.totalHammingDistance([4, 14, 2])