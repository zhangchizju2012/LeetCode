#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 11:13:19 2017

@author: zhangchi
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for item in nums:
            if item in dic:
                return True
            else:
                dic[item] = 1
        return False
        