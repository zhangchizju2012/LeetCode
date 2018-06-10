#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 18:32:05 2018

@author: zhangchi
"""

class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        value = 0
        for i in range(len(S)-1,-1,-1):
            value += shifts[i]
            if value >= 26:
                value = value % 26
            shifts[i] = value
        result = ""
        for index, item in enumerate(S):
            value = ord(item) + shifts[index]
            if value > 122:
                value -= 26
            result += chr(value)
        return result
    
s = Solution()
print s.shiftingLetters("abc", [3,5,9])
        