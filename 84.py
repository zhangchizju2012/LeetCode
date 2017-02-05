#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 15:57:35 2017

@author: zhangchi
"""

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights = heights + [0]
        stack = [0]
        maxValue = 0
        for i in range(1,len(heights)):
            if heights[i] >= heights[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                    if len(stack) > 1:
                        value = (i-stack[-2]-1) * heights[stack[-1]]
                    else:
                        value = i * heights[stack[-1]]
                    maxValue = max(maxValue,value)
                    stack.pop()
                stack.append(i)
        return maxValue
        
