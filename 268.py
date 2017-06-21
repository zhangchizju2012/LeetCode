#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 13:08:53 2017

@author: zhangchi
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = set()
        for item in nums:
            dic.add(item)
        for i in xrange(len(nums)+1):
            if i not in dic:
                return i