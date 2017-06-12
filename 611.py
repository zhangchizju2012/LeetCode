#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 20:12:23 2017

@author: zhangchi
"""

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        if length < 3:
            return 0
        tempResult = []
        for i in xrange(length-2):
            first = nums[i]
            pointA = i + 1
            pointB = i + 2
            count = 0
            while pointB < length:
                if first + nums[pointA] > nums[pointB]:
                    count += 1
                    pointB += 1
                else:
                    tempResult.append(count)
                    pointA += 1
                    count -= 1
                    if pointA == pointB:
                        pointB += 1
                        count = 0
            tempResult.append((count+1)*count/2)
        return tempResult, sum(tempResult)
        
s = Solution()
print s.triangleNumber([3,3,4,5,6,7,7,8,9,8,9,10,11,11,12,19,22,24,35,82,84])
                
            