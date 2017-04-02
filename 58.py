#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 23:11:15 2017

@author: zhangchi
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split(' ')
        for i in range(len(words)-1,-1,-1):
            if len(words[i]) > 0:
                return len(words[i])
        return 0