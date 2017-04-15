#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 22:33:28 2017

@author: zhangchi
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:return [1]
        if rowIndex == 1:return [1,1]
        temp = [1,1]
        for i in range(rowIndex-1):
            tempResult = []
            for i in range(len(temp)-1):
                tempResult.append(temp[i]+temp[i+1])
            temp = [1] + tempResult + [1]
        return temp
        
s = Solution()
print s.getRow(2)