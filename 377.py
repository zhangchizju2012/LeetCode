#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 12:04:27 2017

@author: zhangchi
"""
#==============================================================================
# https://leetcode.com/problems/combination-sum-iv/#/solutions
# Think about the recurrence relation first. How does the number of combinations 
# of the target related to the number of combinations of numbers that are smaller 
# than the target?
# 
# So we know that target is the sum of numbers in the array. 
# Imagine we only need one more number to reach target, 
# this number can be any one in the array, right? So the number
#  of combinations of target, comb[target] = sum(comb[target - nums[i]]), 
# where 0 <= i < nums.length, and target >= nums[i].
# 
# In the example given, we can actually find the number of combinations 
# of 4 with the number of combinations of 3(4 - 1), 2(4- 2) and 1(4 - 3). 
# As a result, comb[4] = comb[4-1] + comb[4-2] + comb[4-3] = comb[3] + comb[2] + comb[1].

# 假设是[2,3] 目标是7,
# comb[5] = 2 --> [2,3], [3,2]
# comb[4] = 1 --> [2,2]
# 新加的东西一律放在最前面（随意规定，当然也可以规定一律放在最后面，最后结果是一致的）
#==============================================================================

# dynamic programming
class Solution(object):
    def __init__(self):
        self.dictionary = {0:1}

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        self.helper(nums, target)
        return self.dictionary[target]
        
    def helper(self, nums, target):
        result = 0
        for item in nums:
            if item <= target:
                if target - item not in self.dictionary:
                    self.helper(nums, target - item)
                result += self.dictionary[target - item]
            else:
                break
        self.dictionary[target] = result

#==============================================================================
# # much slower, dfs        
# class Solution(object):
#     def __init__(self):
#         self.result = 0
#         
#     def combinationSum4(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         for item in nums:
#             if item == target:
#                 self.result += 1
#             elif item < target:
#                 self.combinationSum4(nums, target - item)
#         return self.result        
#==============================================================================

s = Solution()
print s.combinationSum4([2,3],7)