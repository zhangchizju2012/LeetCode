#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 16:41:25 2017

@author: zhangchi
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # needle can be any length, even 0, such as ""
        if needle == "":
            return 0
        length = len(needle)
        for i in range(len(haystack)-length+1):
            if haystack[i:i+length] == needle:
                return i
        return -1