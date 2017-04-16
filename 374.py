#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 22:03:36 2017

@author: zhangchi
"""

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        if guess(left) == 0:
            return left
        if guess(right) == 0:
            return right
        while True:
            middle = (left + right) // 2
            temp = guess(middle)
            if temp == 0:
                return middle
            elif temp == 1:
                left = middle
            else:
                right = middle