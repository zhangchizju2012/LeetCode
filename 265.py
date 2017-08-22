#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 12:10:10 2017

@author: zhangchi
"""

class Solution(object):
    # 对比256
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0 or len(costs[0]) == 0:
            return 0
        if len(costs[0]) == 1:
            return costs[0][0]
        length = len(costs[0])
        last = [0] * length
        for item in costs:
            now = []
            minimumTwo = self.findMinimumTwo(last)
            # 其实只要找到最小的两个就行了，可以在O(n)内完成
            for i in xrange(length):
                if last[i] == minimumTwo[0]:
                    now.append(minimumTwo[1]+item[i])
                else:
                    now.append(minimumTwo[0]+item[i])
            last = now
        return min(last)
    
    def findMinimumTwo(self, nums):
        result = [float('inf'),float('inf')]
        for item in nums:
            if item <= result[0]:
                result = [item,result[0]]
            elif item < result[1]:
                result = [result[0],item]
        return result
    
s = Solution()
print s.minCostII([[8]])