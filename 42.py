#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 20:49:05 2017

@author: zhangchi
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = []
        right = []
        leftLargest = 0
        rightLargest = 0
        length = len(height)
        for i in range(length):
            leftLargest = max(leftLargest,height[i])
            left.append(leftLargest)
        for i in range(length-1,-1,-1):
            rightLargest = max(rightLargest,height[i])
            right.append(rightLargest)
        value = 0
        for i in range(length):
            minValue = min(left[i],right[length-i-1])
            if height[i] < minValue:
                value = value + (minValue - height[i])
        return value

S = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print S.trap(height)