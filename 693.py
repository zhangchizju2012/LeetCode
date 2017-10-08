#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 19:31:22 2017

@author: zhangchi
"""

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = 0
        last = None
        value = 2 ** i
        while n > value:
            if n & value > 0:
                if last == None or last == 0:
                    last = 1
                else:
                    return False
            else:
                if last == None or last == 1:
                    last = 0
                else:
                    return False
            i = i + 1
            value = 2 ** i
        return True
    
s = Solution()
print s.hasAlternatingBits(3)
                