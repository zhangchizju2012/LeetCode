#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 12:31:19 2017

@author: zhangchi
"""
# 复习，效率又提高了，而且很容易理解

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        # 答案肯定在第一个到倒数第二个 和 第二个到最后一个 这两种之间产生
        return max(self.helper(nums[:-1]),self.helper(nums[1:]))
        
    def helper(self, nums):
        # 就是198.py里的新方法，只是换了个function名字
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


#==============================================================================
# """
# Created on Fri Dec 30 16:28:05 2016
# 
# @author: zhangchi
# """
# 
# #可以的，AC了
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
#     def rob1(self, nums):
#         self.dictionary = [-1] * len(nums)
#         return self.helpRob(nums)
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         #因为首尾相连了，所以第一家和最后一家只能抢其中的一家，或者都不抢 much faster
#         if len(nums) == 0:
#             return 0
#         return max(self.rob1(nums[1:-1]), nums[0] + self.rob1(nums[2:-1]), nums[-1] + self.rob1(nums[1:-2]))
#         '''too slow 每一组都分析过去
#         if len(nums) == 0:
#             return 0
#         maxValue = -1
#         for i in range(len(nums)):
#             value = nums[i] + self.rob1(nums[i+2:max(i+2+len(nums)-3,len(nums)-1)]+nums[max(0,i+2-len(nums)):max(i-1,0)])
#             if value > maxValue:
#                 maxValue = value
#         return maxValue
#         '''
#==============================================================================
        
S = Solution()
nums = [2]
print S.rob(nums)