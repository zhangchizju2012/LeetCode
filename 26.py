#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 11:25:44 2017

@author: zhangchi
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) >= 1:
            point = 1
            for index,item in enumerate(nums):
                if index >= 1:
                    if nums[index] != nums[index-1]:
                        nums[point] = nums[index]
                        point += 1
            return point
        else:
            return 0
        
# =============================================================================
# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) >= 1:
#             previous = nums[0]
#             index = 0
#             for i in xrange(1,len(nums)):
#                 if nums[i] != previous:
#                     nums[index] = previous
#                     index += 1
#                     previous = nums[i]
#             nums[index] = previous
#             return index + 1
#         else:
#             return 0
# =============================================================================
            
s = Solution()
print s.removeDuplicates([1,1,2,3,3])