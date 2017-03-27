#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 22:18:44 2017

@author: zhangchi
"""

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = {}
        result = []
        for i in range(len(s)-9):
            if s[i:i+10] in dic:
                dic[s[i:i+10]] += 1
            else:
                dic[s[i:i+10]] = 1
        for item in dic:
            if dic[item] > 1:
                result.append(item)
        return result
        
s = Solution()
print s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAA")