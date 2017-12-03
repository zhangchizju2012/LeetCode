#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 20:23:21 2017

@author: zhangchi
"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0] * len(temperatures)
        stack = []
        for index, item in enumerate(temperatures):
            if len(stack) == 0:
                stack.append([index, item])
            else:
                while len(stack) > 0 and item > stack[-1][1]:
                    compareIndex, _ = stack.pop()
                    result[compareIndex] = index - compareIndex
                stack.append([index, item])
        return result
    
s = Solution()
print s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
                