#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 01:25:42 2017

@author: zhangchi
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dictR = {}
        for item in ransomNote:
            if item in dictR:
                dictR[item] += 1
            else:
                dictR[item] = 1
        dictM = {}
        for item in magazine:
            if item in dictM:
                dictM[item] += 1
            else:
                dictM[item] = 1
        for item in dictR:
            if item not in dictM or dictM[item] < dictR[item]:
                return False
        return True