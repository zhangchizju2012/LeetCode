#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 19:28:32 2017

@author: zhangchi
"""

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        for item in nums:
            if len(result) == 0:
                result.append(item)
            elif len(result) == 1:
                if item > result[0]:
                    result = [item] + result
                else:
                    result.append(item)
            else:
                if item > result[0]:
                    result = [item] + [result[0]]
                elif item > result[1]:
                    result[1] = item
        if len(result) == 1 or result[0] >= 2 * result[1]:
            return nums.index(result[0])
        else:
            return -1
        
s = Solution()
print s.dominantIndex([1, 2, 3, 4])