#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 11:45:15 2017

@author: zhangchi
"""

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        else:
            return max(len(a),len(b))