#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 11:56:51 2016

@author: zhangchi
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        length = len(str(x))
        for i in range(length/2):
            temp = x/(10**(length-i-1))
            x = x - temp * (10**(length-i-1))
            x = x - temp * (10**i)
            if x%(10**(i+1)) != 0:
                return False
        return True
        
S = Solution()
print S.isPalindrome(12345321)