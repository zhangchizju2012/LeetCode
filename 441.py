#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 01:10:28 2017

@author: zhangchi
"""

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        step = 0
        value = 0
        while value < n:
            step += 1
            value += step
        if value == n:
            return step
        else:
            return step - 1