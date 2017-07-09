#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 21:51:33 2017

@author: zhangchi
"""

class Solution(object):
    # 91的后续
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.dic ={}
        self.s = s
        self.mod = 10**9 + 7
        length = len(s)
        if length == 0:
            return 0
        elif s[0] == "0":
            return 0
        else:
            for i in xrange(length+1):
                self.helper(i)
            return self.helper(length)
        
    def helper(self, length):
        if length == 0:
            return 1
        elif self.s[-length] == "0":
            return 0
        elif length == 1:
            if self.s[-length] == "*":
                return 9
            else:
                return 1
        else:
            if length not in self.dic:
                if self.s[-length] in "12":
                    if self.s[-length+1] == "0" or (self.s[-length] == "2" and self.s[-length+1] in "789"):
                        value = self.helper(length-2)
                    elif self.s[-length+1] == "*":
                        if self.s[-length] == "1":
                            value = 9 * self.helper(length-2) + self.helper(length-1)
                        else:
                            value = 6 * self.helper(length-2) + self.helper(length-1)
                    else:
                        value = self.helper(length-2) + self.helper(length-1)
                elif self.s[-length] == "*":
                    if self.s[-length+1] in "123456":
                        value = 2 * self.helper(length-2) + 9 * self.helper(length-1)
                    elif self.s[-length+1] == "0":
                        value = 2 * self.helper(length-2)
                    elif self.s[-length+1] != "*":
                        value = self.helper(length-2) + 9 * self.helper(length-1)
                    else:
                        value = 15 * self.helper(length-2) + 9 * self.helper(length-1)
                else:
                    value = self.helper(length-1)
                value = value % self.mod
                self.dic[length] = value
            return self.dic[length]

s = Solution()
print s.numDecodings("*")