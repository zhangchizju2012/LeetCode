#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 16:00:00 2017

@author: zhangchi
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for item in s:
            if item in dic:
                dic[item] += 1
            else:
                dic[item] = 1
        result = 0
        label = False
        for i in dic:
            item = dic[i]
            if item % 2 == 1:
                label = True
                result += item - 1
            else:
                result += item
        if label:
            return result + 1
        else:
            return result
            
s = Solution()
print s.longestPalindrome("abccccdd")