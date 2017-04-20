#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 21:24:03 2017

@author: zhangchi
"""

import random

class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        index = []
        for i, item in enumerate(self.nums):
            if item == target:
                index.append(i)
        return index[random.randint(0,len(index)-1)]

nums = [1,2,3,3,3]
target = 1                 
obj = Solution(nums)
print obj.pick(target)