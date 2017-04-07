#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 15:49:42 2017

@author: zhangchi
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        string = ''
        length = 0
        result = 0
        for item in s:
            if item not in string:
                string += item
                length += 1
            else:
                position = string.find(item)
                string = string[position+1:] + item
                length = len(string)
            result = max(result,length)
        return result