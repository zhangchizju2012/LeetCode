#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 13:21:24 2017

@author: zhangchi
"""

class Solution(object):
    def helper(self,temp):
        result = ""
        previous = temp[0]
        count = 1
        for item in xrange(1,len(temp)):
            if temp[item] == previous:
                count += 1
            else:
                result += str(count) + previous
                previous = temp[item]
                count = 1
        result += str(count) + previous
        return result
        
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        else:
            origin = "1"
            count = 1
            while count < n:
                count += 1
                origin = self.helper(origin)
            return origin
            
s = Solution()
print s.countAndSay(111)
                
                