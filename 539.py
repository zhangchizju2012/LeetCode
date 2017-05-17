#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 14:50:54 2017

@author: zhangchi
"""

class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        timeList = []
        for item in timePoints:
            timeList.append(int(item[:2])*60+int(item[-2:]))
        timeList.sort()
        timeList.append(timeList[0]+1440)
        difference = float('inf')
        for i in xrange(len(timeList)-1):
            difference = min(difference,timeList[i+1]-timeList[i])
        return difference