#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 18:36:09 2018

@author: zhangchi
"""

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for item in S:
            if item == "(":
                stack.append("(")
            else:
                if stack[-1] == "(":
                    value = 1
                    stack.pop()
                    if len(stack) > 0:
                        item = stack[-1]
                        if item == "(":
                            stack.append(value)
                        else:
                            stack[-1] += value
                    else:
                        stack.append(value)
                else:
                    value = stack.pop() * 2
                    stack.pop()
                    if len(stack) > 0:
                        item = stack[-1]
                        if item == "(":
                            stack.append(value)
                        else:
                            stack[-1] += value
                    else:
                        stack.append(value)
        return stack[-1]
    
s = Solution()
print s.scoreOfParentheses("(()(()))")