#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 21:51:57 2017

@author: zhangchi
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        return self.maxProduct_help(nums)[0]
    def maxProduct_help(self, nums):
        if len(nums) == 1:
            if nums[0] < 0:
                return (0,nums[0])
            else:
                return (nums[0],0)
        else:
            middle = len(nums)//2
            left = self.maxProduct_help(nums[:middle])
            right = self.maxProduct_help(nums[middle:])
            middleRightNegative = 0
            middleRightPositive = 0
            temp = 1
            for item in nums[middle:]:
                temp *= item
                if temp > middleRightPositive:
                    middleRightPositive = temp
                if temp < middleRightNegative:
                    middleRightNegative = temp
            middleLeftNegative = 0
            middleLeftPositive = 0
            temp = 1
            for i in range(len(nums[:middle])-1,-1,-1):
                temp *= nums[:middle][i]
                if temp > middleLeftPositive:
                    middleLeftPositive = temp
                if temp < middleLeftNegative:
                    middleLeftNegative = temp
            return (max(left[0],right[0],middleLeftPositive*middleRightPositive,middleLeftNegative*middleRightNegative),min(left[1],right[1],middleLeftNegative*middleRightPositive,middleRightNegative*middleLeftPositive))
            
s = Solution()
print s.maxProduct([2,3,-2,4])