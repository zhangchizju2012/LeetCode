#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 20:49:46 2017

@author: zhangchi
"""

# 关键就是给定一串数，是否有子集的和能与给定值相同
# 最开始时候我自己的想法是产生所有的子集(用dfs,或这bit manipulation的方法)，然后与target对比

#==============================================================================
# 由这题产生了新的产生子集的思路
# nums=[1,2,3,4]
# previous = [[]]
# for item in nums:
#     temp = []
#     for number in previous:
#         temp.append(number + [item])
#     previous = previous + temp
# 最后所有子集就在previous里
#==============================================================================

class Solution(object):
    # inspired by https://discuss.leetcode.com/topic/67539/0-1-knapsack-detailed-explanation
    # but improved this solution a lot.
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total / 2
        previous = {0:1} # improved by adding hashmap compared with the sencond.
        for item in nums:
            temp = {}
            for number in previous:
                if number + item == target:
                    return True
                elif number + item not in previous: # 可以进一步优化，当number + item > target，就可以扔掉了
                    temp[number + item] = 1
            previous.update(temp) # combine two dictionary
        return False

#==============================================================================
# class Solution(object):
#     def canPartition(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         total = sum(nums)
#         if total % 2 == 1:
#             return False
#         target = total / 2
#         previous = [0]
#         for item in nums:
#             temp = []
#             for number in previous:
#                 if number + item == target:
#                     return True
#                 elif number + item not in previous: # improved by checking "in previous" compared with the third.
#                     temp.append(number + item)
#             previous = previous + temp
#         return False
#==============================================================================

#==============================================================================
# class Solution(object):
#     # slow, brute force
#     def canPartition(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         total = sum(nums)
#         if total % 2 == 1:
#             return False
#         target = total / 2
#         previous = [0]
#         for item in nums:
#             temp = []
#             for number in previous:
#                 if number + item == target:
#                     return True
#                 else:
#                     temp.append(number + item)
#             previous = previous + temp
#         return False
#==============================================================================

s = Solution()
print s.canPartition([100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100])