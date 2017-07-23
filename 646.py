#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 19:35:09 2017

@author: zhangchi
"""

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x:x[0])
        pairs.sort(key=lambda x:x[1])
        previous = pairs[0][1]
        result = 1
        for i in xrange(1,len(pairs)):
            if pairs[i][0] > previous:
                result += 1
                previous = pairs[i][1]
        return result
        
s = Solution()
print s.findLongestChain([[1,2]])
                