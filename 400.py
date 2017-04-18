#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 12:08:27 2017

@author: zhangchi
"""

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = 9
        count = 1
        while n > 0:
            n -= temp * count
            temp *= 10
            count += 1
        temp /= 10
        count -= 1
        n += temp * count
        number = (n - 1) // count
        position = (n - 1) % count
        string = str(10**(count-1)+number)
        return int(string[position])
        
s = Solution()
print s.findNthDigit(3)