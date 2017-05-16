#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 10:54:08 2017

@author: zhangchi
"""

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        lengthG = len(g)
        lengthS = len(s)
        if lengthG == 0 or lengthS == 0:
            return 0
        g.sort()
        s.sort()
        pointG = 0
        pointS = 0
        result = 0
        while pointG < lengthG and pointS < lengthS:
            if g[pointG] <= s[pointS]:
                result += 1
                pointG += 1
                pointS += 1
            else:
                pointS += 1
        return result
        
s = Solution()
print s.findContentChildren([1,2], [1,2,3])