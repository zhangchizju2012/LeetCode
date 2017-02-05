#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 20:56:53 2016

@author: zhangchi
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return
        if length == 1:
            return nums[0]
        middle_index = length/2
        left = self.maxSubArray(nums[:middle_index])
        right = self.maxSubArray(nums[middle_index:])
        
        leftWithMid = 0
        maxLeftWithMid = 0
        leftLable = True
        for i in range(middle_index-1,-1,-1):
            leftWithMid = leftWithMid + nums[i]
            if leftWithMid > maxLeftWithMid:
                maxLeftWithMid = leftWithMid
                leftLable = False
                
        rightWithMid = 0
        maxRightWithMid = 0
        rightLabel = True
        for i in range(middle_index,length):
            rightWithMid = rightWithMid + nums[i]
            if rightWithMid > maxRightWithMid:
                maxRightWithMid = rightWithMid
                rightLabel = False
        
        if leftLable and rightLabel:#避免出现一个元素都不取的情况，如[-1,-2]时候
            value = max(nums[middle_index-1],nums[middle_index])
        else:
            value = maxLeftWithMid + maxRightWithMid
        
        return max(left,right,value)
        
S = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print S.maxSubArray(nums)