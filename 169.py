#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 22:09:44 2017

@author: zhangchi
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        length = len(nums)/2.
        for item in nums:
            if item in dic:
                dic[item] += 1
            else:
                dic[item] = 1
            if dic[item] > length:
                    return item