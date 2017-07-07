#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 15:40:28 2017

@author: zhangchi
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        temp = {}
        result = []
        for item in nums1:
            temp[item] = 1
        for item in nums2:
            if item in temp and temp[item] == 1:
                result.append(item)
                temp[item] -= 1
        return result
        
s = Solution()
print s.intersection([1, 2, 2, 1],[2, 2])