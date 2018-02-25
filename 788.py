#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 19:30:59 2018

@author: zhangchi
"""

class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.stop = set([3,4,7])
        self.go = set([2,5,6,9])
        
        count = 0
        for i in range(1,N+1):
            if self.helper(i):
                count += 1
        return count
            
    def helper(self, val):
        lable = False
        while val != 0:
            temp = val % 10
            if temp in self.stop:
                return False
            if temp in self.go:
                lable = True
            val = val // 10
        return lable
    
s = Solution()
print s.rotatedDigits(10)