#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 21:46:23 2017

@author: zhangchi
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        temp = 1
        for i in range(len(digits)-1,-1,-1):
            if digits[i] + temp >= 10:
                digits[i] = (digits[i] + temp) % 10
                temp = 1
            else:
                digits[i] += temp
                return digits
        if temp == 1:
            return [1] + digits