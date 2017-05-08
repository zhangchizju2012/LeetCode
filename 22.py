#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 22:32:39 2017

@author: zhangchi
"""

class Solution(object):
    def __init__(self):
        self.result = []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.length = 2 * n
        self.helper("",n,n)
        return self.result
    
    def helper(self,string,plus,minus):
        if self.length == len(string):
            self.result.append(string)
        else:
            if plus == minus:
                # “("一定要比"）"多
                self.helper(string+"(",plus-1,minus)
            else:
                if plus >= 1:
                    self.helper(string+"(",plus-1,minus)
                if minus >= 1:
                    self.helper(string+")",plus,minus-1)
s = Solution()
print s.generateParenthesis(6)