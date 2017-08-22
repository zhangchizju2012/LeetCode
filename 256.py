#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 11:44:53 2017

@author: zhangchi
"""

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0 or len(costs[0]) == 0:
            return 0
        last = [0,0,0]
        for item in costs:
            now = [0,0,0]
            now[0] = min(last[1],last[2]) + item[0]
            now[1] = min(last[0],last[2]) + item[1]
            now[2] = min(last[0],last[1]) + item[2]
            last = now
        return min(last)
    
s = Solution()
print s.minCost([[7,6,2],[3,2,4],[7,6,2],[3,2,4]])