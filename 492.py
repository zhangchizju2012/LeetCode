#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 21:41:59 2017

@author: zhangchi
"""
import math

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        for i in range(int(math.sqrt(area)),0,-1):
            if area % i == 0:
                return [area/i,i]