#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 14:54:01 2016

@author: zhangchi
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return 2
        self.dictionary = {1:1,2:2}
        return self.helpClimbStairs(n)
    def helpClimbStairs(self,n):
        if n-1 in self.dictionary:
            temp1 = self.dictionary[n-1]
        else:
            temp1 = self.helpClimbStairs(n-1)
            self.dictionary[n-1] = temp1

        if n-2 in self.dictionary:
            temp2 = self.dictionary[n-2]
        else:
            temp2 = self.helpClimbStairs(n-2)
            self.dictionary[n-2] = temp2
        
        return temp1 + temp2
        
        
        
