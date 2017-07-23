#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 19:42:56 2017

@author: zhangchi
"""

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        result = length
        for l in xrange(2,length+1):
            for i in xrange(0,length-l+1):
                sub = s[i:i+l]
                if sub == sub[::-1]:
                    result += 1
        return result
        
s = Solution()
print s.countSubstrings("abc")