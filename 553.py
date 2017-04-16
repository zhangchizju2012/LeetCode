#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 19:25:34 2017

@author: zhangchi
"""

class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 1:
            return str(nums[0])
        elif len(nums) == 2:
            return str(nums[0]) +'/'+str(nums[1])
        else:
            result = ""
            for i in range(len(nums)):
                if i == 0:
                    result += str(nums[0]) + '/('
                elif i == len(nums) - 1:
                    result += str(nums[len(nums) - 1]) + ')'
                else:
                    result += str(nums[i]) + '/'
            return result