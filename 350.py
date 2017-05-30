#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 10:23:33 2017

@author: zhangchi
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        for item in nums1:
            if item in dic:
                dic[item] += 1
            else:
                dic[item] = 1
        result = []
        for item in nums2:
            if item in dic and dic[item] > 0:
                result.append(item)
                dic[item] -= 1
        return result