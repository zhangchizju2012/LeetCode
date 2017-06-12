#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 15:32:04 2017

@author: zhangchi
"""

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dicS = {}
        dicT = {}
        for item in s:
            if item in dicS:
                dicS[item] += 1
            else:
                dicS[item] = 1
        for item in t:
            if item in dicT:
                dicT[item] += 1
            else:
                dicT[item] = 1
        for item in dicT:
            if (item not in dicS) or (dicT[item] > dicS[item]):
                return item