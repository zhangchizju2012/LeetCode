#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 19:46:50 2017

@author: zhangchi
"""

class Solution(object):
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        dic = {}
        key = 10
        value = 9
        while value <= n:
            dic[value] = key
            key *= 10
            value *= 9
        value /= 9
        result = 0
        while n > 9:
            result += (n//value) * dic[value]
            n = n % value
            value /= 9
        return result + self.helper(n)
    
    def helper(self,n):
        if n <= 8:
            return n
        if n == 9:
            return 10
    
s = Solution()
for i in xrange(983,0,-1):
    print str(i)+": "
    print s.newInteger(i)
        