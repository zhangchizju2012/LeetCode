#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 19:45:50 2018

@author: zhangchi
"""

class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        distance = abs(target[0]) + abs(target[1])
        for item in ghosts:
            if abs(item[0]-target[0]) + abs(item[1]-target[1]) <= distance:
                return False
        return True
    
s = Solution()
print s.escapeGhosts([[1,9],[2,-5],[3,8],[9,8],[-1,3]],[8,-10])