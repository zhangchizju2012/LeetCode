#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:46:36 2017

@author: zhangchi
"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        s_list =[]
        while i < len(s):
            if s[i] == ' ':
                i += 1
            elif s[i] in '+-*/':
                s_list.append(s[i])
                i += 1
            else:
                temp = s[i]
                i += 1
                while i < len(s) and s[i] not in ' +-*/':
                    temp += s[i]
                    i += 1
                s_list.append(temp)
        # get postfix expression
        tempResult = []
        operator = []
        for item in s_list:
            if item in '+-':
                while len(operator) > 0:#pay attention, not if, once made mistakes here
                    tempResult.append(operator.pop())
                operator.append(item)
            elif item in '*/':
                while len(operator) > 0 and operator[-1] in '*/':
                    #pay attention, not if, once made mistakes here
                    tempResult.append(operator.pop())
                operator.append(item)
            else:
                tempResult.append(item)
        while len(operator) > 0:
            tempResult.append(operator.pop())
        # calculate 
        stack = []
        for item in tempResult:
            if item in '+-*/':
                tempA = stack.pop()
                tempB = stack.pop()
                if item == '+':
                    stack.append(tempB+tempA)
                elif item == '-':
                    stack.append(tempB-tempA)
                elif item == '*':
                    stack.append(tempB*tempA)
                elif item == '/':
                    stack.append(tempB//tempA)
            else:
                stack.append(int(item))
        return stack[-1]
    
s = Solution()
print s.calculate("1*2+9/  10   -3/4+5*6-7*8 ")