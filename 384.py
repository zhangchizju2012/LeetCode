#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 13:57:24 2017

@author: zhangchi
"""
import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.order = range(len(nums))
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        random.shuffle(self.order) # 只要产生一个就行了，如果要自己打乱顺序而不用random.shuffle可以用random.randint来循环把index拿到
        return [self.nums[index] for index in self.order]

# =============================================================================
# class Solution(object):
# 
#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         self.nums = nums
#         self.label = False
#         self.result = []
#         
# 
#     def reset(self):
#         """
#         Resets the array to its original configuration and return it.
#         :rtype: List[int]
#         """
#         return self.nums
#         
# 
#     def shuffle(self):
#         """
#         Returns a random shuffling of the array.
#         :rtype: List[int]
#         """ # 产生了所有的可能排列，产生过一次了就不再产生，但在这个问题中其实不需要全部产生
#         if self.label == False:
#             if len(self.nums) == 1:
#                 self.result = [[self.nums[0]]]
#             else:
#                 for i in xrange(len(self.nums)):
#                     for possibility in self.helper(self.nums[:i]+self.nums[i+1:]):
#                         self.result.append([self.nums[i]]+possibility)
#             self.label = True
#         if len(self.result) == 0:
#             return []
#         else: 
#             return self.result[random.randint(0,len(self.result)-1)]
#                     
#     def helper(self, nums):
#         if len(nums) == 1:
#             return [[nums[0]]]
#         result = []
#         for i in xrange(len(nums)):
#             for possibility in self.helper(nums[:i]+nums[i+1:]):
#                 result.append([nums[i]]+possibility)
#         return result
# =============================================================================
                    
# 产生所有的排列组合
# =============================================================================
# class Solution(object):
#     def shuffle(self, nums):
#         if len(nums) == 1:
#             return [[nums[0]]]
#         result = []
#         for i in xrange(len(nums)):
#             for possibility in self.shuffle(nums[:i]+nums[i+1:]):
#                 result.append([nums[i]]+possibility)
#         return result
# =============================================================================
    
s = Solution()
print s.shuffle([])
        