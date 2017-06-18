#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 19:29:20 2017

@author: zhangchi
"""

class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        minValue = float('inf')
        minIndex = []
        maxValue = -float('inf')
        maxIndex = []
        for index,item in enumerate(arrays):
            if item[0] < minValue:
                minValue = item[0]
                minIndex = [index]
            elif item[0] == minValue:
                minIndex.append(index)
                
            if item[-1] > maxValue:
                maxValue = item[-1]
                maxIndex = [index]
            elif item[-1] == maxValue:
                maxIndex.append(index)
        if len(maxIndex) > 1 or len(minIndex) > 1 or minIndex[0] != maxIndex[0]:
            return maxValue - minValue
        else:
            tempMax = maxValue
            tempMin = minValue
            tempIndex = minIndex[0]

            minValue = float('inf')
            minIndex = []
            maxValue = -float('inf')
            maxIndex = []
            for index,item in enumerate(arrays):
                if index != tempIndex:
                    if item[0] < minValue:
                        minValue = item[0]
                        minIndex = [index]
                    elif item[0] == minValue:
                        minIndex.append(index)
                        
                    if item[-1] > maxValue:
                        maxValue = item[-1]
                        maxIndex = [index]
                    elif item[-1] == maxValue:
                        maxIndex.append(index)
            return max(tempMax-minValue,maxValue-tempMin)
            
s = Solution()
print s.maxDistance([[2,2,3],[1,5],[2,2,3]])