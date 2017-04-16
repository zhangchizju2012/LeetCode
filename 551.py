#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 19:24:46 2017

@author: zhangchi
"""

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = 0
        countL = 0
        for i in s:
            if i == "A":
                count += 1
                countL = 0
            elif i == "L":
                countL += 1
            else:
                countL = 0
            if count > 1:
                return False
            if countL > 2:
                return False
        return True