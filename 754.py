#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 23:57:53 2018

@author: zhangchi
"""

class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        now = [0]
        step = 1
        while True:
            future = []
            for item in now:
                candidate = item + step
                if candidate == target:
                    return step
                else:
                    future.append(candidate)
                    
                candidate = item - step
                if candidate == target:
                    return step
                else:
                    future.append(candidate)
            now = future
            step += 1