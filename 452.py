#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 17:41:46 2017

@author: zhangchi
"""


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x:x[1])
        end = -float('inf')
        result = 0
        for a,b in points:
            if a > end:
                result += 1
                end = b
        return result