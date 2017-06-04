#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 19:29:42 2017

@author: zhangchi
"""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed = [1,0] + flowerbed + [0,1]
        indexList= []
        for index, item in enumerate(flowerbed):
            if item == 1:
                indexList.append(index)
        temp = []
        for i in xrange(len(indexList)-1):
            temp.append(indexList[i+1]-indexList[i]-1)
        total = 0
        for item in temp:
            if item > 0:
                total += (item-1) // 2
        return total >= n
            
s = Solution()
print s.canPlaceFlowers([1,1,1,1,1,1,1,1,1,1,1,1,1],0)