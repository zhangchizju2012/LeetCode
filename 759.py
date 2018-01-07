#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 20:01:28 2018

@author: zhangchi
"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def employeeFreeTime(self, avails):
        """
        :type avails: List[List[Interval]]
        :rtype: List[Interval]
        """
        positionList = []
        
        for people in avails:
            for interval in people:
                positionList.append([interval.start,interval.end])
                #positionList.append([interval[0],interval[1]])
        
        positionList.sort(key=lambda x:x[1])
        positionList.sort(key=lambda x:x[0])
        #print positionList
        
        result = []
        for item in positionList:
            if len(result) == 0:
                result.append(item)
            else:
                if result[-1][0] <= item[0] <= result[-1][1]:
                    result[-1][1] = max(result[-1][1], item[1])
                else:
                    result.append(item)
                    
        if len(result) < 2:
            return []
        else:
            output = []
            for i in xrange(len(result)-1):
                output.append([result[i][1],result[i+1][0]])
            return output
        
s = Solution()
print s.employeeFreeTime([[[1,2],[5,6]],[[1,3]],[[4,10]]])
print s.employeeFreeTime([[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]])