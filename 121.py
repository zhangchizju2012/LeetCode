#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 13:25:46 2016

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
        low = prices[0]
        result = 0
        for item in prices:
            if item < low:
                low = item
            result = max(result,item-low)
        return result
    
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length == 1 or length == 0:
            return 0
        elif length == 2:
            return max(prices[1] - prices[0],0)
        middle = length/2
        left = self.maxProfit(prices[:middle])
        right = self.maxProfit(prices[middle:])
        
        leftMin = float('inf')
        for i in range(middle):
            if prices[i] < leftMin:
                leftMin = prices[i]

        rightMax = -float('inf')
        for i in range(middle,length):
            if prices[i] > rightMax:
                rightMax = prices[i]
    
        return max(left,right,max(0,rightMax-leftMin))
        
S = Solution()
prices = [7, 6, 4, 3, 1]
print S.maxProfit(prices)