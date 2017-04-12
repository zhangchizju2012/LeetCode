#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 14:46:25 2017

@author: zhangchi
"""

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        elements = [0] * len(words)
        for i in range(len(words)):
            for chara in words[i]:
                elements[i] |= 1 << (ord(chara) - 97)
        
        result = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if elements[i] & elements[j] == 0:
                    result = max(result, len(words[i]) * len(words[j]))
        return result
                