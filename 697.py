#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 19:32:33 2017

@author: zhangchi
"""

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        result = []
        degree = 0
        for index, item in enumerate(nums):
            if item not in dic:
                dic[item] = [index]
            else:
                dic[item].append(index)
            if len(dic[item]) > degree:
                degree = len(dic[item])
                result = [dic[item]]
            elif len(dic[item]) == degree:
                result.append(dic[item])
        final = float('inf')
        for item in result:
            final = min(final, item[-1]-item[0]+1)
        return final 
    
s = Solution()
print s.findShortestSubArray([1, 2, 2, 3, 1])
            