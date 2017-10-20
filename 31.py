#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 23:00:59 2017

@author: zhangchi
"""

# 按照2413， 2431这两个例子试试就行了 （多试试几个例子就明白了）
# 从右到左，发现出现一个数变小了，那就说明该数加上后面的部分可以调整了
# 没有出现变小的数，都不能调整

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        label = True
        for i in xrange(len(nums)-1,-1,-1):
            if i == len(nums)-1 or nums[i] >= nums[i+1]:
                pass
            else:
                nums[i+1:] = nums[i+1:][::-1]
                for j in xrange(i+1, len(nums)):
                    if nums[j] > nums[i]:
                        nums[j], nums[i] = nums[i], nums[j]
                        label = False
                        break
                break
        if label is True:
            nums.sort()
    
# =============================================================================
#     def nextPermutation(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         previous = []
#         for i in xrange(len(nums)-1,-1,-1):
#             if len(previous) == 0 or nums[i] >= previous[-1]:
#                 previous.append(nums[i])
#             else:
#                 temp = nums[:i]
#                 tempValue = nums[i]
#                 for i in xrange(len(previous)):
#                     if previous[i] > tempValue:
#                         index = i
#                         break
#                 tempValue, previous[index] = previous[index], tempValue
#                 return temp + [tempValue] + previous
#         return previous
# =============================================================================
    
s = Solution()
print s.nextPermutation([])