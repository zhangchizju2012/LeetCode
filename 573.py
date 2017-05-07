#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 10:19:34 2017

@author: zhangchi
"""

class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        result = 0
        distance1 = []
        distance2 = []
        for a,b in nuts:
            temp1 = abs(a-tree[0]) + abs(b-tree[1])
            result += temp1
            distance1.append(temp1)
            temp2 = abs(a-squirrel[0]) + abs(b-squirrel[1])
            distance2.append(temp2)
        temp = -float('inf')
        for a,b in zip(distance1,distance2):
            temp = max(temp,a-b)
        return 2*result-temp
        
s = Solution()
print s.minDistance(5,7,[2,2],[4,4],[[3,0]])