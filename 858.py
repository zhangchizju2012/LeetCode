#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 19:11:14 2018

@author: zhangchi
"""

class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        temp = self.gcd(p, q)
        p = p // temp
        q = q // temp
        if q % 2 == 0:
            return 0
        else:
            if p % 2 == 1:
                return 1
            else:
                return 2


    def gcd(self, a, b):
        a, b = (a, b) if a >=b else (b, a)
        while b:
            a, b = b, a % b
        return a
    
s = Solution()
print s.mirrorReflection(1,2)