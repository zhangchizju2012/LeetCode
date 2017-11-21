#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 22:53:19 2017

@author: zhangchi
"""

from random import randint
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(nums, l, r):
            ri = randint(l, r)
            nums[ri], nums[r] = nums[r], nums[ri]
            for i, val in enumerate(nums[l:r+1], l):
                if val >= nums[r]:
                    nums[l], nums[i] = nums[i], nums[l]
                    l += 1
            return l-1
        
        l = 0
        r = len(nums)-1
        k = k-1
        while l <= r:
            pos = partition(nums, l, r)
            if pos > k:
                r = pos - 1
            elif pos < k:
                l = pos + 1
            else:
                return nums[pos]