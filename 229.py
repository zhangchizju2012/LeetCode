#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 09:52:04 2017

@author: zhangchi
"""

class Solution(object):
    # inspired by https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        candidate1 = None
        candidate2 = None # two candidates instead of one candidate is the difference.
        count1 = 0
        count2 = 0
        for item in nums:
            if count1 <= 0 and candidate2 != item: # <= instead of == is the difference
                candidate1 = item
            elif count2 <= 0 and candidate1 != item:
                candidate2 = item
            if candidate1 == item:
                count1 += 2 # 2 instead of 1 is the difference.
                count2 -= 1
            elif candidate2 == item:
                count2 += 2
                count1 -= 1
            else:
                count1 -= 1
                count2 -= 1
        count1 = 0
        count2 = 0
        for item in nums:
            if item == candidate1:
                count1 += 1
            elif item == candidate2:
                count2 += 1
        threshold = len(nums) / 3.0
        result = []
        if count1 > threshold:
            result.append(candidate1)
        if count2 > threshold:
            result.append(candidate2)
        return result
        
s = Solution()
print s.majorityElement([1,1,1,3,3,2,2,2])

#==============================================================================
# Boyer-Moore Algorithm
# candidate = 0
# count = 0
# for value in input:
#   if count == 0:
#     candidate = value
#   if candidate == value:
#     count += 1
#   else:
#     count -= 1
#==============================================================================
      
# another solution      
class Solution:
# @param {integer[]} nums
# @return {integer[]}
    def majorityElement(self, nums):
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1 # use 1, but no -1 for count2, this is the difference
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2)
                        if nums.count(n) > len(nums) // 3]