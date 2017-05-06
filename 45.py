#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 09:38:51 2017

@author: zhangchi
"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums) - 1
        if nums[0] >= length:
            return 1
        previous = 0
        now = nums[0]
        temp = - float('inf')
        count = 1
        while True:
            count += 1
            for i in xrange(previous+1,now+1):
                temp = max(temp, i+nums[i])
                if temp >= length:
                    return count
            previous = now
            now = temp