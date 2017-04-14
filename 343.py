#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 01:27:31 2017

@author: zhangchi
"""

# other solutions with mathmatics provement
# https://discuss.leetcode.com/topic/45341/a-simple-explanation-of-the-math-part-and-a-o-n-solution
# https://discuss.leetcode.com/topic/43055/why-factor-2-or-3-the-math-behind-this-problem/5

class Solution(object):
    def __init__(self):
        self.dictionary = {2:1}

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.dictionary:
            return self.dictionary[n]
        else:
            temp = 1
            for i in range(1,n-1):
                temp = max(temp, max(i,self.integerBreak(i)) * max(n-i,self.integerBreak(n-i)))
            self.dictionary[n] = temp
            # if n == 1, it should be 1 (or less), so temp = 1 can be changed to temp = 0.5 ...
            # max(1,self.integerBreak(1))) should be 1, guarantee this, then ok
            return temp