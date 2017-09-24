#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 19:33:10 2017

@author: zhangchi
"""

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        result = 0
        validList = []
        for item in ops:
            if item.isdigit() or item[0]=="-":
                value = int(item)
                validList.append(value)
                result += value
            elif item == "C":
                value = validList.pop()
                result -= value
            elif item == "D":
                value = validList[-1] * 2
                validList.append(value)
                result += value
            else:
                value = validList[-1] + validList[-2]
                validList.append(value)
                result += value
        return result
    
s = Solution()
print s.calPoints(["5","2","C","D","+"])