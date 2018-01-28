#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 19:44:18 2018

@author: zhangchi
"""

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        dic = {}
        for item in J:
            dic[item] = 0
        total = 0
        for item in S:
            if item in dic:
                total += 1
        return total
    
s = Solution()
print s.numJewelsInStones("aA", "aAAbbbb")