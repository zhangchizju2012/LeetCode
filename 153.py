#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 17:29:09 2017

@author: zhangchi
"""

#==============================================================================
# think about these possibilities
# 0,1,2,3,4,5,6
# 1,2,3,4,5,6,0
# 2,3,4,5,6,0,1
# 3,4,5,6,0,1,2
# 4,5,6,0,1,2,3
# 5,6,0,1,2,3,4
# 6,0,1,2,3,4,5
# if the middle one is larger than the left the one and the right one, than the
# min value should between the middle one and the larger of one (among left one and right one)
# if the middle one is smaller than the left the one and the right one, than the
# min value should between the middle one and the smaller of one (among left one and right one)
# the left one is always bigger than the right one if the min value is not the left one
#
# important properties for Rotated Sorted Array
#==============================================================================

# By myself without help

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        middle = (left + right) // 2
        while True:
            if nums[left] < nums[left-1]:
                return nums[left]
            if nums[right] < nums[right-1]:
                return nums[right]
            #if nums[left] <= nums[right]:#it won't exist because of the former 2 if sentences
            # the left one is always bigger than the right one if the min value is not the left one
            #    return nums[left]
            #else:
            if nums[middle] > nums[left]:
                left = middle
            else:
                right = middle
            middle = (left + right) // 2
            