#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 19:28:40 2017

@author: zhangchi
"""

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        value = []
        for item in nums:
            if item not in dic:
                dic[item] = 1
                value.append(item)
            else:
                dic[item] += 1
        if len(value) <= 1:
            return 0
        value.sort()
        maxValue = -float('inf')
        for i in xrange(len(value)-1):
            if value[i+1] - value[i] == 1:
                maxValue = max(maxValue,dic[value[i]]+dic[value[i+1]])
        if maxValue == -float('inf'):
            maxValue = 0
        return maxValue
        
s = Solution()
print s.findLHS([1,3,5,7,9,11,13,15,17])