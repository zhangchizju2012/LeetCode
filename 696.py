#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 19:44:33 2017

@author: zhangchi
"""

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = []
        previous = s[0]
        count = 1
        for i in xrange(1, len(s)):
            if s[i] == previous:
                count += 1
            else:
                temp.append(count)
                previous = s[i]
                count = 1
        temp.append(count)
        
        result = 0
        
        for i in xrange(len(temp)-1):
            result += min(temp[i], temp[i+1])
        
        return result
    
s = Solution()
print s.countBinarySubstrings("0")