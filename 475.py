#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 01:15:58 2017

@author: zhangchi
"""

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        result = -float('inf')
        heaters = [-float('inf')] + heaters + [float('inf')] # 前后加的float('inf')为了配合后面
        index = 0
        for item in houses:
            while heaters[index] < item: # 找到合适的对比位置
                index += 1
            result = max(result,min(heaters[index]-item,item-heaters[index-1])) # 跟前后的对比就行了
        return result