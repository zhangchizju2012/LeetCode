#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 20:17:01 2017

@author: zhangchi
"""

class Solution(object):
    # 一定要非常注意corner case，像100，110，0开头，含27这种
    # 注意程序中的大量if else
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.dic ={}
        self.s = s
        length = len(s)
        if length == 0:
            return 0
        elif s[0] == "0":
            return 0
        else:
            return self.helper(length)
        
    def helper(self, length):
        if length == 0:
            return 1
        elif self.s[-length] == "0":
            return 0
        elif length == 1:
            return 1
        else:
            if length not in self.dic:
                if self.s[-length] in "12":
                    if self.s[-length+1] == "0" or (self.s[-length] == "2" and self.s[-length+1] in "789"):
                        value = self.helper(length-2)
                    else:
                        value = self.helper(length-2) + self.helper(length-1)
                else:
                    value = self.helper(length-1)
                self.dic[length] = value
            return self.dic[length]
                
s = Solution()
print s.numDecodings("110")
# 100; 110
            