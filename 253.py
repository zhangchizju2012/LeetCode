#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 22:38:04 2017

@author: zhangchi
"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
# =============================================================================
#     def minMeetingRooms(self, intervals):
#         """
#         :type intervals: List[Interval]
#         :rtype: int
#         """
#         if len(intervals) == 0:
#             return 0
#         intervals.sort(key=lambda x:x[0])
#         last = [intervals[0][1]]
#         for i in xrange(1,len(intervals)):
#             here = intervals[i][0]
#             label = False
#             for j in xrange(len(last)):
#                 if here >= last[j]:
#                     last[j] = intervals[i][1]
#                     label = True
#                     break
#             if label is False:
#                 last.append(intervals[i][1])
#         return len(last)
# =============================================================================
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x:x.start)
        last = [intervals[0].end]
        for i in xrange(1,len(intervals)):
            here = intervals[i].start
            label = False
            for j in xrange(len(last)):
                if here >= last[j]:
                    last[j] = intervals[i].end
                    label = True
                    break
            if label is False:
                last.append(intervals[i].end)
        return len(last)
    
s = Solution()
print s.minMeetingRooms([[1,5],[8,9],[8,9]])