#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 19:32:03 2017

@author: zhangchi
"""

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        dic = set()
        for i in xrange(c+1):
            temp = i**2
            if temp <= c:
                dic.add(temp)
            else:
                break
        for i in dic:
            if c - i in dic:
                return True
        return False
        
s = Solution()
print s.judgeSquareSum(1)