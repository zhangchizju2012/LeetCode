#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 19:00:33 2018

@author: zhangchi
"""

class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        dic = {}
        number = []
        for item in hand:
            if item not in dic:
                dic[item] = 1
                number.append(item)
            else:
                dic[item] += 1
        number.sort()
        
        for item in number:
            value = dic[item]
            if value > 0:
                for i in range(W):
                    if item+i not in dic or dic[item+i] < value:
                        return False
                    else:
                        dic[item+i] -= value
        return True
    
s = Solution()
print s.isNStraightHand([1,2,3,4,5],  4)