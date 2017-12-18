#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 19:29:23 2017

@author: zhangchi
"""

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        result = [0] * len(cost)
        for i in xrange(2,len(cost)):
            result[i] = min(result[i-1]+cost[i-1],result[i-2]+cost[i-2])
        return min(result[-1]+cost[-1],result[-2]+cost[-2])
    
s = Solution()
print s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])