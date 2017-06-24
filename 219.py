#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 11:17:26 2017

@author: zhangchi
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for index, item in enumerate(nums):
            if item not in dic:
                dic[item] = index
            else:
                if index - dic[item] <= k:
                    return True
                else:
                    dic[item] = index
        return False