#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 01:06:59 2017

@author: zhangchi
"""
# 复习

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        length = len(nums) + 1
        dp = [0] * length
        dp[1] = nums[0]
        for i in xrange(1,len(nums)):
            dp[i+1] = max(dp[i], dp[i-1]+nums[i])
        return dp[-1]

s = Solution()
print s.rob()

#==============================================================================
# """
# Created on Fri Dec 30 15:27:57 2016
# 
# @author: zhangchi
# """
# # 可以的，AC了
# 
# class Solution(object):
#     def helpRob(self, nums):
#         if len(nums) == 0:
#             return 0
#         elif len(nums) == 1:
#             value = nums[0]
#             self.dictionary[0] = value
#             return value
#         if self.dictionary[len(nums)-1] != -1:
#             return self.dictionary[len(nums)-1]
#         else:
#             value = max(self.helpRob(nums[1:]),self.helpRob(nums[2:])+nums[0])
#             self.dictionary[len(nums)-1] = value
#             return value
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         self.dictionary = [-1] * len(nums)
#         return self.helpRob(nums)
#     
#==============================================================================
