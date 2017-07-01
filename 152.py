#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Created on Sat Jul  1 13:24:29 2017

@author: zhangchi
"""

#复习
class Solution(object):
    # 自己也想到了要构造minValue, maxValue, 想到了会出现负数的问题，还想到了出现（-1，1）的数的问题
    # 但是没想到出现（-1，1）的数的问题如何解决，答案是通过line28,29解决的，而且其实是出现（-1，1）的数时没有
    # 立即解决，其实是到(-1，1）的数的下一个数时，通过max/min来把前面的问题解决
    # 最后看了这个链接写出来的 https://discuss.leetcode.com/topic/4417/possibly-simplest-solution-with-o-n-time-complexity
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = nums[0]
        minValue = temp
        maxValue = temp
        result = temp
        for i in xrange(1,len(nums)):
            if nums[i] < 0:
                minValue, maxValue = maxValue, minValue
            minValue = min(minValue*nums[i],nums[i])
            maxValue = max(maxValue*nums[i],nums[i])
            result = max(result,maxValue)
        return result
#==============================================================================
# """
# Created on Thu Mar 30 21:51:57 2017
# 
# @author: zhangchi
# """
# # AC了，可行
# 
# class Solution(object):
#     def maxProduct(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) == 1:
#             return nums[0]
#         return self.maxProduct_help(nums)[0]
#     def maxProduct_help(self, nums):
#         # it can calculate the maximum value as well as minimum value at the same time
#         # the largest/smallest value is generated in the left part, the right part
#         # or in the middle part
#         if len(nums) == 1:
#             if nums[0] < 0:
#                 return (0,nums[0])
#             else:
#                 return (nums[0],0)
#         else:
#             middle = len(nums)//2
#             left = self.maxProduct_help(nums[:middle])
#             right = self.maxProduct_help(nums[middle:])
#             middleRightNegative = 0
#             middleRightPositive = 0
#             temp = 1
#             for item in nums[middle:]:
#                 temp *= item
#                 if temp > middleRightPositive:
#                     middleRightPositive = temp
#                 if temp < middleRightNegative:
#                     middleRightNegative = temp
#             middleLeftNegative = 0
#             middleLeftPositive = 0
#             temp = 1
#             for i in range(len(nums[:middle])-1,-1,-1):
#                 temp *= nums[:middle][i]
#                 if temp > middleLeftPositive:
#                     middleLeftPositive = temp
#                 if temp < middleLeftNegative:
#                     middleLeftNegative = temp
#             return (max(left[0],right[0],middleLeftPositive*middleRightPositive,middleLeftNegative*middleRightNegative),min(left[1],right[1],middleLeftNegative*middleRightPositive,middleRightNegative*middleLeftPositive))
#             
#==============================================================================
s = Solution()
print s.maxProduct([2,3,-2,4])