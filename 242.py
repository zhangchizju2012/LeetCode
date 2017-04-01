#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 22:49:31 2017

@author: zhangchi
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sDict = {}
        for i in s:
            if i in sDict:
                sDict[i] += 1
            else:
                sDict[i] = 1
        tDict = {}
        for i in t:
            if i in tDict:
                tDict[i] += 1
            else:
                tDict[i] = 1
        for item in sDict:
            if item not in tDict or tDict[item] != sDict[item]:
                return False
            tDict[item] = 0
        for item in tDict:
            if tDict[item] != 0:
                return False
        return True