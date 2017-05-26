#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 21:45:40 2017

@author: zhangchi
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for count, item in enumerate(s[::-1]):
            result += (ord(item) - ord('A') + 1) * (26 ** count)
        return result
        
s = Solution()
print s.titleToNumber('')