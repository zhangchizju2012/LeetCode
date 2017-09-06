#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 22:32:40 2017

@author: zhangchi
"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if len(intervals) == 0:
            return True
        intervals.sort(key=lambda x:x.start)
        last = intervals[0].end
        for i in xrange(1,len(intervals)):
            if intervals[i].start >= last:
                last = intervals[i].end
            else:
                return False
        return True