#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 19:30:06 2017

@author: zhangchi
"""

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        label = True
        result = 0
        before = float('inf')
        for item in prices:
            if item > before:
                if label is True:
                    result += item - before
                    before = item
                    label = False
                else:
                    result += item - before
                    before = item
                
            if item + fee < before:
                before = item + fee
                label = True
        return result
    
s = Solution()
print s.maxProfit([], 2)
            