#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 20:03:45 2017

@author: zhangchi
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for item in tokens:
            if item in "+-/*":
                a = stack.pop()
                b = stack.pop()
                if item == '+':
                    stack.append(a+b)
                elif item == '-':
                    stack.append(b-a)
                elif item == '*':
                    stack.append(a*b)
                elif item == '/':
                    if b//a < 0:#(-9)//12 = -1(it should be 0)
                        stack.append(-(-b//a))
                    else:
                        stack.append(b//a)
            else:
                stack.append(int(item))
        return stack[0]

s = Solution()
print s.evalRPN(["4","-2","/","2","-3","-","-"])