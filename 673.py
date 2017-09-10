#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 20:03:27 2017

@author: zhangchi
"""

# 在300.py的基础上改的 其实自己也想到了的
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        length = len(nums)
        result = [1] * length
        countList = [1] * length # 用来储存可能存在的个数
        
        for i in xrange(length-2,-1,-1):
            temp = - float('inf')
            count = 1
            for j in xrange(i+1,length):
                if nums[i] < nums[j]:
                    if temp < result[j]:
                        temp = result[j]
                        count = countList[j]
                    elif temp == result[j]:
                        count += countList[j]
            if temp > 0:
                result[i] = temp + 1
                countList[i] = count
        maxValue = max(result)
        returnResult = 0
        for index,item in enumerate(result):
            if item == maxValue:
                returnResult += countList[index]
        return returnResult#, returnResult, countList
    
s = Solution()
print s.findNumberOfLIS([1,1,1,1])