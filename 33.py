#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:14:46 2017

@author: zhangchi
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        l = 0
        r = length - 1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            else:
                if nums[m] > nums[l]:
                    if nums[l] < target < nums[m]:
                        r = m - 1
                    else:
                        l = m + 1
                else:
                    if nums[m] < target < nums[r]:
                        l = m + 1
                    else:
                        r = m - 1
        return -1
# http://fisherlei.blogspot.ca/2013/01/leetcode-search-in-rotated-sorted-array.html        
s = Solution()
print s.search([4, 5, 6, 7, 0, 1, 2],4)
