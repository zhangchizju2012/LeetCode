#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 19:42:50 2017

@author: zhangchi
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        result = 0
        last = prices[0]
        for item in prices:
            if item >= last:
                result += (item - last)
                last = item
            else:
                last = item
        return result