#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  10 12:01:25 2017

@author: zhangchi
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(1)
            elif s[i] == '[':
                stack.append(2)
            elif s[i] == '{':
                stack.append(3)
            elif len(stack) == 0:
                return False
            elif s[i] == ')' and stack[-1] == 1:
                stack.pop()
            elif s[i] == ']' and stack[-1] == 2:
                stack.pop()
            elif s[i] == '}' and stack[-1] == 3:
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False