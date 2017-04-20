#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 22:35:31 2017

@author: zhangchi
"""
#==============================================================================
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/#/solutions
# def minMoves2(self, nums):
#     median = sorted(nums)[len(nums) / 2]
#     return sum(abs(num - median) for num in nums)
# 
# def minMoves2(self, nums):
#     nums.sort()
#     return sum(nums[~i] - nums[i] for i in range(len(nums) / 2))
#==============================================================================

class Solution(object):            
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        dictionary = {}
        itemList = []
        for item in nums:
            if item in dictionary:
                dictionary[item] += 1
            else:
                dictionary[item] = 1
                itemList.append(item)                
        itemList.sort()
        
        left = 0
        leftCount = 0
        right = 0
        rightCount = 0
        for item in itemList:
            right += dictionary[item] * abs(item - itemList[0])
            if item > itemList[0]:
                rightCount += dictionary[item]
        now = left + right
            
        for i in range(1,len(itemList)):
            leftCount += dictionary[itemList[i-1]]
            left +=  leftCount * (itemList[i] - itemList[i-1])
            right -= rightCount * (itemList[i] - itemList[i-1])
            rightCount -= dictionary[itemList[i]]
            # draw a ficture, 柱状图， 从左到右依次变大，then you will understand what happens here.
            if left + right < now:
                now = left + right
            else:
                return now
        return 0

# improved from original solution, which is quite slow!
        
#==============================================================================
# class Solution(object):
#     def getValue(self, direction, temp):
#         value = 0
#         if direction == 'l':
#             for item in self.dictionary:
#                 if item < temp:
#                     value += self.dictionary[item] * abs(item - temp)
#         else:
#             for item in self.dictionary:
#                 if item > temp:
#                     value += self.dictionary[item] * abs(item - temp)
#         return value
#             
#     def minMoves2(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) == 1:
#             return 0
#         self.dictionary = {}
#         itemList = []
#         for item in nums:
#             if item in self.dictionary:
#                 self.dictionary[item] += 1
#             else:
#                 self.dictionary[item] = 1
#                 itemList.append(item)
#         itemList.sort()
#         previous = float('inf')
#         for item in itemList:
#             now =  self.getValue('l',item) + self.getValue('r',item) # improve this part!
#             if now < previous:
#                 previous = now
#             else:
#                 return previous
#         return 0
#==============================================================================
                
s = Solution()
#a = [10,10,3,4,2,7,5,23,6,45,34,3,9,56]
print s.minMoves2([10,10,3,4,2,7,5,23,6,45,34,3,9,56])