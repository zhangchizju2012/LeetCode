#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 20:27:30 2017

@author: zhangchi
"""

# 整体思路：
# 每k个求和（这是之前的一道常规题），然后从求和出来的数中，找三个数（这三个数两两的index之差需要超过k）使和最大
# 基本思路是，三个数，以中间这个数为分界线（向左向右都隔开k），前面找最大的，后面也找最大的

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        temp = []
        temp.append(sum(nums[:k]))
        for i in xrange(k,len(nums)):
            temp.append(temp[-1]+nums[i]-nums[i-k])
            
        leftMax = {}
        # 从左往右考虑，到i这个index处，最大的数是啥，对应的index是啥
        maxValue = -float('inf')
        maxIndex = -float('inf')
        for index, item in enumerate(temp):
            if item > maxValue:
                maxValue = item
                maxIndex = index
            leftMax[index] = [maxValue, maxIndex]
            
        rightMax = {}
        # 从右往左考虑
        maxValue = -float('inf')
        maxIndex = -float('inf')
        for index in xrange(len(temp)-1,-1,-1):
            if temp[index] >= maxValue:
                maxValue = temp[index]
                maxIndex = index
            rightMax[index] = [maxValue, maxIndex]
            
        maxValue = -float('inf')
        for i in xrange(k, len(temp)-k):
            value = leftMax[i-k][0] + temp[i] + rightMax[i+k][0]
            # 分别代表左边的最大，中间的数，右边的最大，减掉或者加上的k就是分割开的间隔
            if value > maxValue: 
                maxValue = value
                result = [leftMax[i-k][1],i,rightMax[i+k][1]]
        return result
    
s = Solution()
#print s.maxSumOfThreeSubarrays([11,17,4,11],1)
print s.maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2)