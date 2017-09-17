#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 20:07:30 2017

@author: zhangchi
"""

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = 0
        return self.helper(s, stack)
        
    def helper(self, s, stack):
        if stack + self.count(s,"(") > self.count(s,")") + self.count(s,"*"):
            return False
        length = len(s)
        for i in xrange(length):
            if s[i] == "(":
                stack += 1
            elif s[i] == ")":
                if stack == 0:
                    return False
                else:
                    stack -= 1
            else:
                if self.helper(s[i+1:],stack+1):
                    return True
                elif self.helper(s[i+1:],stack):#会影响stack
                    return True
                elif stack > 0 and self.helper(s[i+1:],stack-1):
                    return True
                return False
        return stack == 0
    
    def count(self, s, label):
        c = 0
        for item in s:
            if item == label:
                c += 1
        return c
                
s = Solution()
print s.checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())")
print s.checkValidString("((*)")