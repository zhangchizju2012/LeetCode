#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 01:15:13 2017

@author: zhangchi
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if int(str(abs(x))[::-1]) >= 2 ** 31:
            return 0
        else:
            if x >= 0:
                return int(str(x)[::-1])
            else:
                return -int(str(-x)[::-1])