#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 10:42:35 2017

@author: zhangchi
"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        temp = x ^ y
        result = 0
        for i in xrange(32):
            if (2**i) & temp > 0:
                result += 1
        return result