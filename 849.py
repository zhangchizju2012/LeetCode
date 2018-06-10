#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 18:41:34 2018

@author: zhangchi
"""

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        temp = []
        for index, item in enumerate(seats):
            if item == 1:
                temp.append(index)
        if len(temp) == 1:
            return max(temp[0], len(seats)-temp[0]-1)
        else:
            maxValue = -float('inf')
            for i in range(len(temp)-1):
                if temp[i+1] - temp[i] > maxValue:
                    maxValue = temp[i+1] - temp[i]
            return max(temp[0], len(seats)-temp[-1]-1, maxValue//2)
        
s = Solution()
print s.maxDistToClosest([1,0,0,0])