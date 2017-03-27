#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 23:36:18 2017

@author: zhangchi
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n!=0:
            if n%2 == 1:
                count += 1
            n=n//2
        return count
        
s = Solution()
print s.hammingWeight(1)