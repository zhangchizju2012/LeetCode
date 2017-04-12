#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 18:44:23 2017

@author: zhangchi
"""


# http://www.programcreek.com/2015/04/leetcode-power-of-four-java/
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        temp = 1
        while temp < num:
            temp *= 4
        if temp == num:
            return True
        else:
            return False
                