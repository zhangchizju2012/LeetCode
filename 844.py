#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 18:31:24 2018

@author: zhangchi
"""

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stack1 = []
        for item in S:
            if item == "#":
                if len(stack1) > 0:
                    stack1.pop()
            else:
                stack1.append(item)
        stack2 = []
        for item in T:
            if item == "#":
                if len(stack2) > 0:
                    stack2.pop()
            else:
                stack2.append(item)
        return stack1 == stack2
    
s = Solution()
print s.backspaceCompare("a#c",  "b")