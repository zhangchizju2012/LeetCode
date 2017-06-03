#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 16:59:18 2017

@author: zhangchi
"""

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp = []
        while num > 0:
            temp.append(num%2)
            num = num // 2
        result = 0
        for i in xrange(len(temp)):
            result += (temp[i] ^ 1) * (2 ** i)
        return result
        
s = Solution()
print s.findComplement(1)