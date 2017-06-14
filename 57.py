#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 13:10:18 2017

@author: zhangchi
"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
class Solution(object):
    # 跟616后面部分一致
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x.start)
        result = [intervals[0]]
        for i in xrange(1,len(intervals)):
            if result[-1].start <= intervals[i].start <= result[-1].end:
                result[-1].end = max(result[-1].end,intervals[i].end)
            else:
                result.append(intervals[i])
        return result
#==============================================================================
# # list version, exactly the same
# class Solution(object):
#     def insert(self, intervals, newInterval):
#         """
#         :type intervals: List[Interval]
#         :type newInterval: Interval
#         :rtype: List[Interval]
#         """
#         intervals.append(newInterval)
#         intervals.sort(key=lambda x:x[0])
#         result = [intervals[0]]
#         for i in xrange(1,len(intervals)):
#             if result[-1][0] <= intervals[i][0] <= result[-1][1]:
#                 result[-1][1] = max(result[-1][1],intervals[i][1])
#             else:
#                 result.append(intervals[i])
#         return result
#         
# s = Solution()
# print s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,9])
#==============================================================================
        